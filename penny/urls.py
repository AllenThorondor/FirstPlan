from django.urls import path
from .views import (
    StiverListView,
    StiverDetailView,
    StiverCreateView,
    StiverUpdateView,
    StiverDeleteView,
    StiverFocusView,
    )
from . import views


urlpatterns = [
    path('', StiverListView.as_view(), name = "penny-home"),
    path('stiver/<int:pk>/', StiverDetailView.as_view(), name = "stiver-detail"),
    path('stiver/new/', StiverCreateView.as_view(), name = "stiver-create"),
    path('stiver/<int:pk>/update', StiverUpdateView.as_view(), name = "stiver-update"),
    path('stiver/<int:pk>/delete', StiverDeleteView.as_view(), name = "stiver-delete"),
    path('focus', StiverFocusView.as_view(), name = "stiver-create"),
    ]
