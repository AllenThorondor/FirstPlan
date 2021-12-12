from django.shortcuts import render, redirect, get_object_or_404
from .models import Plan
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from . import views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.db import connection
from taggit.models import Tag


# Create your views here.
def home(request):
    context = {
    'plans'     :   Plan.objects.all()
    }
    return render(request, 'plans/home.html', context)

def PlanCheck(*args, **kwargs):

    Plan.objects.filter(pk=kwargs['pk']).update(plan_state=1)
    #Plan.plan_check()
    #messages.success(request, f'状态已更新完成!')
    return redirect('plan-home')

def PlanUncheck(*args, **kwargs):

    Plan.objects.filter(pk=kwargs['pk']).update(plan_state=0)
    #Plan.plan_check()
    #messages.success(request, f'状态已更新完成!')
    return redirect('plan-home')


class PlanListView(LoginRequiredMixin, ListView):
    model = Plan
    template_name = 'plans/home.html'
    context_object_name = 'plans'
    ordering = ['-date_created']
    #paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plans'] = Plan.objects.filter(plan_state=0)
        return context


class CompletedPlanListView(LoginRequiredMixin, ListView):
    model = Plan
    template_name = 'plans/home.html'
    context_object_name = 'completed_plans'
    ordering = ['-date_created']
    #paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['completed_plans'] = Plan.objects.filter(plan_state=1)
        return context


class PlanDetailView(LoginRequiredMixin, DetailView):
    model = Plan


class PlanCreateView(LoginRequiredMixin, CreateView):
    model = Plan
    fields = ['plan_detail', 'tags']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PlanUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Plan
    fields = ['plan_detail', 'plan_state', 'tags']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        plan = self.get_object()
        if self.request.user == plan.author:
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

def tagged(request, pk):
    tag = get_object_or_404(Tag, id=pk)
    common_tags = Plan.tags.most_common()[:4]
    plans = Plan.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'common_tags':common_tags,
        'plans':plans,
    }
    return render(request, 'plans/home.html', context)
