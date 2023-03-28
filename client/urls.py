from django.urls import path
from .views import (
    CompanyListView,
    CompanyCreateView,
    CompanyUpdateView,
    CompanyDeleteView)
from . import views

urlpatterns = [
    path('', CompanyListView.as_view(), name = "company-home"),
    #path('user/<str:username>', UserPostListView.as_view(), name = "user-posts"),
    path('company/<int:pk>/', views.company_detail_view, name = "company-detail"),
    path('company/new/', CompanyCreateView.as_view(), name = "company-create"),
    path('company/<int:pk>/update/', CompanyUpdateView.as_view(), name = "company-update"),
    path('company/<int:pk>/delete/', CompanyDeleteView.as_view(), name = "company-delete"),
    #path('about/', views.about, name = "blog-about"),
    path('tag/<int:pk>/', views.tagged, name="company-tagged"),
    path('company/<int:pk>/add', views.add_company_update, name = "company-add"),
]
