from django.urls import path
from . import views
from .views import (
    RecordDetailView,
    RecordUpdateView,
    RecordDeleteView,
)


urlpatterns = [
    path('', views.home, name = "health-home"),
    path('health/<int:pk>/', RecordDetailView.as_view(), name = "health-detail"),
    path('health/<int:pk>/update', RecordUpdateView.as_view(), name = "health-update"),
    path('health/<int:pk>/delete', RecordDeleteView.as_view(), name = "health-delete"),
    path('add/', views.add, name = "health-add"),
    ]
