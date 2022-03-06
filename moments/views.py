from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from django.contrib.auth.decorators import login_required
from .models import (
    Collection,
    CollectionImage,
    Person,
    PersonImage,
    Event,
    EventImage)
from .forms import CollectionImageForm, PersonImageForm, EventImageForm
from django.http import HttpResponse

# exhibition code here.
def index(request):
    context = {
                'collections': Collection.objects.all(),
                'persons':Person.objects.all(),
                'events':Event.objects.all()
              }
    return render(request, 'moments/index.html', context)

def collection_shop(request, pk, *args, **kwargs):
    collection = get_object_or_404(Collection, id = pk)
    photos = CollectionImage.objects.filter(collection=collection)

    context = {
                'photos' : photos
    }
    return render(request, 'moments/shop.html', context)

def person_shop(request, pk, *args, **kwargs):
    person = get_object_or_404(Person, id = pk)
    photos = PersonImage.objects.filter(person=person)

    context = {
                'photos' : photos
    }
    return render(request, 'moments/shop.html', context)

def event_shop(request, pk, *args, **kwargs):
    event = get_object_or_404(Event, id = pk)
    photos = EventImage.objects.filter(event=event)

    context = {
                'photos' : photos
    }
    return render(request, 'moments/shop.html', context)


# collection code here.
class CollectionCreateView(LoginRequiredMixin, CreateView):
    model = Collection
    fields = ['collection_name', 'collection_num', 'discription', 'note', 'cover_image']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CollectionListView(LoginRequiredMixin, ListView):
    model = Collection
    template_name = 'moments/home.html'
    context_object_name = 'collections'
    ordering = ['-date_created']
    paginate_by = 10

class CollectionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Collection
    fields = ['collection_name', 'collection_num', 'discription', 'note', 'cover_image']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        collection = self.get_object()
        if self.request.user == collection.author:
            return True
        return False

class CollectionImageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CollectionImage
    fields = ['collection', 'image', 'story']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        collection_image = self.get_object()
        if self.request.user == collection_image.collection.author:
            return True
        return False

class CollectionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Collection
    success_url = '/moments/home'
    def test_func(self):
        collection = self.get_object()
        if self.request.user == collection.author:
            return True
        return False

class CollectionImageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CollectionImage
    success_url = '/moments/home'
    def test_func(self):
        collection_image = self.get_object()
        if self.request.user == collection_image.collection.author:
            return True
        return False

@login_required
def collection_detail_view(request, pk, *args, **kwargs):
    collection = get_object_or_404(Collection, id = pk)
    photos = CollectionImage.objects.filter(collection=collection)
    return render(request, 'moments/collection_detail.html', {
        'collection' : collection,
        'photos' : photos
    })

@login_required
def collection_image_detail_view(request, pk, *args, **kwargs):
    info = get_object_or_404(CollectionImage, id = pk)
    photo = CollectionImage.objects.filter(id=pk)
    return render(request, 'moments/collectionimage_detail.html', {
        'info' : info,
        'photos' : photo
    })

def add_collection(request, *args, **kwargs):
    if request.method =='POST':
        l_form = CollectionImageForm(request.POST, request.FILES)
        if l_form.is_valid():
            l_form.save()
            messages.success(request, f'your image have beed added, good job!')
    else:
        l_form = CollectionImageForm()
    return render(request, 'moments/add.html', {'form' : l_form})


# person code here.
class PersonCreateView(LoginRequiredMixin, CreateView):
    model = Person
    fields = ['person_name', 'person_num', 'discription', 'note', 'cover_image']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PersonListView(LoginRequiredMixin, ListView):
    model = Person
    template_name = 'moments/person_home.html'
    context_object_name = 'persons'
    ordering = ['-date_created']
    paginate_by = 10

class PersonDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Person
    success_url = '/moments/home'
    def test_func(self):
        person = self.get_object()
        if self.request.user == person.author:
            return True
        return False

class PersonUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Person
    fields = ['person_name', 'person_num', 'discription', 'note', 'cover_image']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        person = self.get_object()
        if self.request.user == person.author:
            return True
        return False

@login_required
def person_detail_view(request, pk, *args, **kwargs):
    person = get_object_or_404(Person, id = pk)
    photos = PersonImage.objects.filter(person=person)
    return render(request, 'moments/person_detail.html', {
        'person' : person,
        'photos' : photos
    })

def add_person(request, *args, **kwargs):
    if request.method =='POST':
        l_form = PersonImageForm(request.POST, request.FILES)
        if l_form.is_valid():
            l_form.save()
            messages.success(request, f'your image have beed added, good job!')
    else:
        l_form = PersonImageForm()
    return render(request, 'moments/add.html', {'form' : l_form})


# event code here.
class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['event_name', 'event_num', 'discription', 'note', 'cover_image']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['event_name', 'event_num', 'discription', 'note', 'cover_image']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
            return True
        return False

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/moments/home'
    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
            return True
        return False

class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'moments/event_home.html'
    context_object_name = 'events'
    ordering = ['-date_created']
    paginate_by = 10

@login_required
def event_detail_view(request, pk, *args, **kwargs):
    event = get_object_or_404(Event, id = pk)
    photos = EventImage.objects.filter(event=event)
    return render(request, 'moments/event_detail.html', {
        'event' : event,
        'photos' : photos
        })

def add_event(request, *args, **kwargs):
    if request.method =='POST':
        l_form = EventImageForm(request.POST, request.FILES)
        if l_form.is_valid():
            l_form.save()
            messages.success(request, f'your image have beed added, good job!')
    else:
        l_form = EventImageForm()
    return render(request, 'moments/add.html', {'form' : l_form})



#example code here
"""
class LaneDetailView(LoginRequiredMixin, DetailView):
    model = Lane

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = LaneImage.objects.filter(lane=lane)
        context['flashes'] = Flash.objects.filter(lane=lane)
        return context

"""
