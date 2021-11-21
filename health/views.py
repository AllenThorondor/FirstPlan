from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Record
from django.http import HttpResponse
from .forms import RecordForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)


# Create your views here.

def home(request):
    context = {
    'records'     :   Record.objects.all()
    }
    return render(request, 'health/home.html', context)


def add(request, *args, **kwargs):
    if request.method =='POST':
        l_form = RecordForm(request.POST, request.FILES)
        if l_form.is_valid():
            l_form.save()
            messages.success(request, f'show yes!')
    else:
        l_form = RecordForm()
    return render(request, 'health/add.html', {'form' : l_form})

class RecordDetailView(LoginRequiredMixin, DetailView):
    model = Record

class RecordUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Record
    fields = ['date', 'score', 'get_bed_time', 'get_up_time','total_time', 'deep_time',
     'light_time', 'dream_time','sober_time', 'snap_time', 'breath_score']
    success_url = '/health'

    """def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        """
    def test_func(self):
        """record = self.get_object()
        if self.request.user == record.author:
            return True"""
        return True


class RecordDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Record
    success_url = '/health'
    def test_func(self):
        """lane = self.get_object()
        if self.request.user == lane.author:
            return True"""
        return True
