from django.urls import path
from .views import (
    PlanListView,
    PlanDetailView,
    PlanCreateView,
    PlanUpdateView,
    PlanDeleteView
    )
from . import views


urlpatterns = [
    path('', PlanListView.as_view(), name = "plan-home"),
    path('plan/<int:pk>/', PlanDetailView.as_view(), name = "plan-detail"),
    path('plan/new/', PlanCreateView.as_view(), name = "plan-create"),
    path('plan/<int:pk>/update', PlanUpdateView.as_view(), name = "plan-update"),
    path('plan/<int:pk>/delete', PlanDeleteView.as_view(), name = "plan-delete"),
]