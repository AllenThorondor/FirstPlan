from django.urls import path
from .views import (
    LaneListView,
    LaneDetailView,
    LaneCreateView,
    LaneUpdateView,
    LaneDeleteView,
    ImageAddView
    )
from . import views


urlpatterns = [
    path('', LaneListView.as_view(), name = "flight-home"),
    path('lane/<int:pk>/', views.detail_view, name = "lane-detail"),
    path('lane/<int:pk>/update', LaneUpdateView.as_view(), name = "lane-update"),
    path('lane/<int:pk>/delete', LaneDeleteView.as_view(), name = "lane-delete"),
    path('lane/<int:pk>/add', ImageAddView.as_view(), name = "lane-add"),
    path('lane/new/', LaneCreateView.as_view(), name = "lane-create"),
    #path('about/', views.about, name = "flight-about")
]
