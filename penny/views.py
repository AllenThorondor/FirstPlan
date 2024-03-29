from django.shortcuts import render
from .models import Stiver, Tag
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from . import views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
def home(request):
    context = {
    'stivers'     :   Stiver.objects.all()
    }
    return render(request, 'penny/home.html', context)

class StiverListView(LoginRequiredMixin, ListView):
    model = Stiver
    template_name = 'penny/home.html'
    context_object_name = 'stivers'
    ordering = ['-date_created']
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        #user = get_object_or_404(User, username=self.kwargs.get('username'))
        #request.user
        return Stiver.objects.filter(author=self.request.user).order_by('-date_created')


class StiverFocusView(LoginRequiredMixin, ListView):
    model = Stiver
    template_name = 'penny/focus/table-row-select.html'
    context_object_name = 'stivers'
    ordering = ['-date_created']
    #paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        #user = get_object_or_404(User, username=self.kwargs.get('username'))
        #request.user
        return Stiver.objects.filter(author=self.request.user).order_by('-date_created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['field_name'] = Stiver._meta.get_fields()
        return context

class StiverDetailView(LoginRequiredMixin, DetailView):
    model = Stiver
    """
    def get_queryset(self):
        laneId = get_object_or_404(Lane, id=self.kwargs.get('id'))
        return Flash.objects.filter(lane=laneId).order_by('-update_time')
        """


class StiverCreateView(LoginRequiredMixin, CreateView):
    model = Stiver
    fields = ['item', 'money', 'note', 'tags']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class StiverUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Stiver
    fields = ['item', 'money', 'note', 'tags']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        stiver = self.get_object()
        if self.request.user == stiver.author:
            return True
        return False


class StiverDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Stiver
    success_url = '/penny'
    def test_func(self):
        stiver = self.get_object()
        if self.request.user == stiver.author:
            return True
        return False
