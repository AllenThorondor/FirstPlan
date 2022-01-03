from django.urls import path
from . import views
from .views import (
    RecordListView,
    RecordDetailView,
    RecordUpdateView,
    RecordDeleteView,
)


urlpatterns = [
    path('', RecordListView.as_view(), name = "health-home"),
    path('health/<int:pk>/', RecordDetailView.as_view(), name = "health-detail"),
    path('health/<int:pk>/update', RecordUpdateView.as_view(), name = "health-update"),
    path('health/<int:pk>/delete', RecordDeleteView.as_view(), name = "health-delete"),
    path('health/add', views.add, name = "health-add"),
    ]
