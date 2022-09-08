from django.urls import path
from .views import (
    CollectionListView,
    PersonListView,
    EventListView,
    CollectionCreateView,
    PersonCreateView,
    EventCreateView,
    CollectionUpdateView,
    CollectionImageUpdateView,
    PersonUpdateView,
    PersonImageUpdateView,
    EventUpdateView,
    EventImageUpdateView,
    CollectionDeleteView,
    CollectionImageDeleteView,
    PersonDeleteView,
    PersonImageDeleteView,
    EventDeleteView,
    EventImageDeleteView
    )
from . import views

urlpatterns = [
    path('', views.index, name = "moments-index"),
    path('shop/<slug:cato>/<int:pk>', views.shop, name = "shop"),
    path('shop/<slug:cato>/<int:pk>/<int:id>', views.single, name = "single"),

    path('home/', CollectionListView.as_view(), name = "moments-home"),
    path('collection/<int:pk>/', views.collection_detail_view, name = "collection-detail"),
    path('collection/<int:pk>/update', CollectionUpdateView.as_view(), name = "collection-update"),
    path('collection/<int:pk>/delete', CollectionDeleteView.as_view(), name = "collection-delete"),
    path('collection/<slug:cato>/<int:pk>/add', views.add_collection, name = "collection-add"),
    path('collection/new/', CollectionCreateView.as_view(), name = "collection-create"),
    path('collection/image/<int:pk>/', views.collection_image_detail_view, name = "collection-image-detail"),
    path('collection/image/<int:pk>/delete', CollectionImageDeleteView.as_view(), name = "collection-image-delete"),
    path('collection/image/<int:pk>/update', CollectionImageUpdateView.as_view(), name = "collection-image-update"),

    path('person/', PersonListView.as_view(), name = "person-home"),
    path('person/<int:pk>/', views.person_detail_view, name = "person-detail"),
    path('person/<int:pk>/update', PersonUpdateView.as_view(), name = "person-update"),
    path('person/<int:pk>/delete', PersonDeleteView.as_view(), name = "person-delete"),
    path('person/<slug:cato>/<int:pk>/add', views.add_person, name = "person-add"),
    path('person/new/', PersonCreateView.as_view(), name = "person-create"),
    path('person/image/<int:pk>/', views.person_image_detail_view, name = "person-image-detail"),
    path('person/image/<int:pk>/delete', PersonImageDeleteView.as_view(), name = "person-image-delete"),
    path('person/image/<int:pk>/update', PersonImageUpdateView.as_view(), name = "person-image-update"),

    path('event/', EventListView.as_view(), name = "event-home"),
    path('event/<int:pk>/', views.event_detail_view, name = "event-detail"),
    path('event/<int:pk>/update', EventUpdateView.as_view(), name = "event-update"),
    path('event/<int:pk>/delete', EventDeleteView.as_view(), name = "event-delete"),
    path('event/<slug:cato>/<int:pk>/add', views.add_event, name = "event-add"),
    path('event/new/', EventCreateView.as_view(), name = "event-create"),
    path('event/image/<int:pk>/', views.event_image_detail_view, name = "event-image-detail"),
    path('event/image/<int:pk>/delete', EventImageDeleteView.as_view(), name = "event-image-delete"),
    path('event/image/<int:pk>/update', EventImageUpdateView.as_view(), name = "event-image-update"),
]
