from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from .models import Lane, Flash
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

class LaneDetailView(LoginRequiredMixin, DetailView):
    model = Lane
    """
    def get_queryset(self):
        laneId = get_object_or_404(Lane, id=self.kwargs.get('id'))
        return Flash.objects.filter(lane=laneId).order_by('-update_time')
        """


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


def add(request, *args, **kwargs):
    if request.method =='POST':
        l_form = FlashForm(request.POST, request.FILES)
        if l_form.is_valid():
            l_form.save()
            messages.success(request, f'Your account has been updated!')
    else:
        l_form = FlashForm()
    return render(request, 'flight/about.html', {'form' : l_form})

class LaneDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Lane
    success_url = '/flight'
    def test_func(self):
        lane = self.get_object()
        if self.request.user == lane.author:
            return True
        return False
