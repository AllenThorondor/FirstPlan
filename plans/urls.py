from django.urls import path
from .views import (
    PlanListView,
    PlanDetailView,
    PlanCreateView,
    PlanUpdateView,
    PlanDeleteView,
    CompletedPlanListView
    )
from . import views


urlpatterns = [
    path('', PlanListView.as_view(), name = "plan-home"),
    path('completed/', CompletedPlanListView.as_view(), name = "completed-plan-home"),
    path('plan/<int:pk>/', PlanDetailView.as_view(), name = "plan-detail"),
    path('plan/new/', PlanCreateView.as_view(), name = "plan-create"),
    path('plan/<int:pk>/update', PlanUpdateView.as_view(), name = "plan-update"),
    path('plan/<int:pk>/delete', PlanDeleteView.as_view(), name = "plan-delete"),
    path('plan/<int:pk>/check', views.PlanCheck, name = 'plan-check'),
    path('plan/<int:pk>/uncheck', views.PlanUncheck, name = 'plan-uncheck'),
    path('tag/<int:pk>/', views.tagged, name="plan-tagged"),
]
