from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView)
from .models import Company, CompanyUpdate
from .forms import CompanyUpdateForm
from taggit.models import Tag
import markdown2


class CompanyListView(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'client/home.html'  #<app>/<model>_<viewtype>.html
    context_object_name = 'companys'
    ordering = ['date_posted']

    def get_queryset(self, *args, **kwargs):
        return Company.objects.filter(author=self.request.user).order_by('-date_posted')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['common_tags'] = Company.tags.most_common()[:10]

        return context



@login_required
def company_detail_view(request, pk, *args, **kwargs):
    company = get_object_or_404(Company, id=pk)
    updates = CompanyUpdate.objects.filter(company=company)
    page = request.GET.get('page')

    return render(request, 'client/company_detail.html', {
        'company' : company,
        'updates'   :   updates,
        'page'  :   page,
    })


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'client/company_detail.html'
    context_object_name = 'company'
    pk_url_kwargs = 'company_id'

    def get_object(self, queryset=None):
        obj = super(CompanyDetailView, self).get_object()
        #obj.story = markdown2.markdown(obj.story, extras=['fenced-code-blocks'], )

        return obj

    def get_context_data(self, **kwargs):
        kwargs['updates'] = self.object.companyupdate_set.all()
        kwargs['form'] = CompanyUpdateForm()

        return super(CompanyDetailView, self).get_context_data(**kwargs)


class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    fields = ['name', 'content', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CompanyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Company
    fields = ['name', 'content', 'address', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        company = self.get_object()
        if self.request.user == company.author:
            return True
        return False


class CompanyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Company
    success_url = '/client'
    def test_func(self):
        company = self.get_object()
        if self.request.user == company.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html',{'title':'About'})

def tagged(request, pk):
    tag = get_object_or_404(Tag, id=pk)
    common_tags = Company.tags.most_common()[:10]

    companys = Company.objects.filter(author=request.user, tags=tag)

    context = {
        'tag':tag,
        'common_tags':common_tags,
        'companys':companys,
    }
    return render(request, 'client/home.html', context)

@login_required
def add_company_update(request, pk, *args, **kwargs):

    if request.method == 'POST':
        l_form = CompanyUpdateForm(request.POST, request.FILES)
        l_form.fields['company'].queryset = Company.objects.filter(id=pk)

        if l_form.is_valid():
            l_form.save()
            messages.success(request, f'更新完成!')
            return redirect('company-detail', pk=pk)
    else:
        l_form = CompanyUpdateForm()
    return render(request, 'client/add.html', {'form' : l_form, 'pk' : pk})

class CompanyProgressView(FormView):
    form_class = CompanyUpdateForm
    template_name = 'client/company_detail.html'

    def form_valid(self, form):
        target_company = get_object_or_404(Company, pk=self.kwargs['company_id'])
        update = form.save(commit=False)

        update.company = target_company
        update.save()

        self.success_url = target_company.get_absolute_url()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        target_company = get_object_or_404(Company, pk=self.kwargs['company_id'])

        return render(self.request, 'client/company_detail.html', {
            'form' : form,
            'company' : target_company,
            'update_list' : target_company.update_set.all()
        })

@login_required
def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = '请输入关键词'
        return render(request, 'client/errors.html', {'error_msg': error_msg})

    company_list = Company.objects.filter(name__icontains=q)
    return render(request, 'client/results.html', {'error_msg': error_msg,
                                               'company_list': company_list})
