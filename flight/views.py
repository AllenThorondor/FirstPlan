from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Lane, Flash, LaneImage
from .forms import FlashForm
from django.http import HttpResponse


def home(request):
    context = {
    'lanes'     :   Lane.objects.all()
    }
    return render(request, 'flight/home.html', context)

class LaneListView(LoginRequiredMixin, ListView):
    model = Lane
    template_name = 'flight/home.html'
    context_object_name = 'lanes'
    ordering = ['-takeoff_time']
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        #user = get_object_or_404(User, username=self.kwargs.get('username'))
        #request.user
        return Lane.objects.filter(author=self.request.user).order_by('-takeoff_time')

@login_required
def detail_view(request, pk, *args, **kwargs):
    lane = get_object_or_404(Lane, id=pk)
    photos = LaneImage.objects.filter(lane=lane)
    flashs = Flash.objects.filter(lane=lane)
    return render(request, 'flight/lane_detail.html', {
        'lane' : lane,
        'photos' : photos,
        'flashs' : flashs
    })

class LaneDetailView(LoginRequiredMixin, DetailView):
    model = Lane

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = LaneImage.objects.filter(lane=lane)
        context['flashes'] = Flash.objects.filter(lane=lane)
        return context




class LaneCreateView(LoginRequiredMixin, CreateView):
    model = Lane
    fields = ['flight_name', 'flight_num', 'provenance', 'destination', 'note', 'picture']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class LaneUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Lane
    fields = ['flight_name', 'flight_num', 'provenance', 'destination', 'note', 'picture']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        lane = self.get_object()
        if self.request.user == lane.author:
            return True
        return False


def add(request, pk, *args, **kwargs):
    if request.method =='POST':
        l_form = FlashForm(request.POST, request.FILES)
        if l_form.is_valid():
            l_form.save()
            messages.success(request, f'your flash have beed added,good job!')
            return redirect('lane-detail', pk=pk)
    else:
        l_form = FlashForm()
    return render(request, 'flight/add.html', {'form' : l_form})


class ImageAddView(LoginRequiredMixin, UserPassesTestMixin, FormView):
    form_class = FlashForm
    template_name = 'flight/add.html'

    def test_func(self):
        post = get_object_or_404(Lane, pk=self.kwargs['pk'])
        if self.request.user == post.author:
            return True
        return False

    def form_valid(self, form):
        target_lane = get_object_or_404(Lane, pk=self.kwargs['pk'])
        update = form.save(commit=False)

        update.lane = target_lane
        update.save()

        self.success_url = target_lane.get_absolute_url()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        target_company = get_object_or_404(Lane, pk=self.kwargs['company_id'])

        return render(self.request, 'client/company_detail.html', {
            'form' : form,
            'company' : target_company,
            'update_list' : target_company.update_set.all()
        })

class LaneDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Lane
    success_url = '/flight'
    def test_func(self):
        lane = self.get_object()
        if self.request.user == lane.author:
            return True
        return False
