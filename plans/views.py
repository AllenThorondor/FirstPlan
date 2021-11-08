from django.shortcuts import render
from .models import Plan
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
    'plans'     :   Plan.objects.all()
    }
    return render(request, 'plans/home.html', context)


class PlanListView(LoginRequiredMixin, ListView):
    model = Plan
    template_name = 'plans/home.html'
    context_object_name = 'plans'
    ordering = ['-date_created']
    paginate_by = 10

class PlanDetailView(LoginRequiredMixin, DetailView):
    model = Plan


class PlanCreateView(LoginRequiredMixin, CreateView):
    model = Plan
    fields = ['plan_detail']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PlanUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Plan
    fields = ['plan_detail']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        stiver = self.get_object()
        if self.request.user == stiver.author:
            return True
        return False


class PlanDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Plan
    success_url = '/plans'
    def test_func(self):
        plan = self.get_object()
        if self.request.user == plan.author:
            return True
        return False
