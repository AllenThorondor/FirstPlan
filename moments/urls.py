from django.urls import path
from .views import (
    CollectionListView,
    #LaneDetailView,
    CollectionCreateView,
    CollectionUpdateView,
    CollectionDeleteView,
    )
from . import views

urlpatterns = [
    path('', views.index, name = "moments-index"),
    path('home/', CollectionListView.as_view(), name = "moments-home"),
    path('collection/<int:pk>/', views.detail_view, name = "collection-detail"),
    path('moments/<int:pk>/', views.shop, name = "moments-detail"),
    path('collection/<int:pk>/update', CollectionUpdateView.as_view(), name = "collection-update"),
    path('collection/<int:pk>/delete', CollectionDeleteView.as_view(), name = "collection-delete"),
    path('collection/<int:pk>/add', views.add, name = "collection-add"),
    path('collection/new/', CollectionCreateView.as_view(), name = "collection-create"),
]
