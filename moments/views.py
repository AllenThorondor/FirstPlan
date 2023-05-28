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
                'events':Event.objects.all().order_by('date_created')
              }
    return render(request, 'moments/index.html', context)

def shop(request, cato, pk, *args, **kwargs):
    if cato == "collection":
        collection = get_object_or_404(Collection, id = pk)
        photos = CollectionImage.objects.filter(collection=collection)

    elif cato == "person":
        person = get_object_or_404(Person, id = pk)
        photos = PersonImage.objects.filter(person=person)

    elif cato == "event":
        event = get_object_or_404(Event, id = pk)
        photos = EventImage.objects.filter(event=event)

    else:
        return render(request, 'blog/about.html',{'title':'About'})

    context = {
                'photos' : photos,
                'cato' : cato,
                'pk' : pk
    }
    return render(request, 'moments/shop.html', context)

def single(request, cato, pk, id, *args, **kwargs):
    if 'collection' in str(request.path):
        photo = get_object_or_404(CollectionImage, id = id)

    elif 'person' in str(request.path):
        photo = get_object_or_404(PersonImage, id = id)

    elif 'event' in str(request.path):
        photo = get_object_or_404(EventImage, id = id)

    else:
        return render(request, 'blog/about.html',{'title':'About'})

    context = {
        'photo' :   photo,
        'cato'  :   cato,
        'pk'    :   pk
    }
    return render(request, 'moments/product-single.html', context)



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

def add_collection(request, cato, pk, *args, **kwargs):
    if request.method =='POST':
        l_form = CollectionImageForm(request.POST, request.FILES)
        l_form.fields['collection'].queryset = Collection.objects.filter(id=pk)
        if l_form.is_valid():
            l_form.save()
            messages.success(request, f'your image have beed added, good job!')
    else:
        l_form = CollectionImageForm()
    return render(request, 'moments/add.html', {'form' : l_form, 'cato' : cato, 'pk' : pk})


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
    success_url = '/moments/person'
    def test_func(self):
        person = self.get_object()
        if self.request.user == person.author:
            return True
        return False

class PersonImageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PersonImage
    success_url = '/moments/person'

    def test_func(self):
        person_image = self.get_object()
        if self.request.user == person_image.person.author:
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

class PersonImageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PersonImage
    fields = ['person', 'image', 'story']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        person_image = self.get_object()
        if self.request.user == person_image.person.author:
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

@login_required
def person_image_detail_view(request, pk, *args, **kwargs):
    info = get_object_or_404(PersonImage, id = pk)
    photo = PersonImage.objects.filter(id=pk)
    return render(request, 'moments/personimage_detail.html', {
        'info' : info,
        'photos' : photo
    })

def add_person(request, cato, pk, *args, **kwargs):
    if request.method =='POST':
        l_form = PersonImageForm(request.POST, request.FILES)
        l_form.fields['person'].queryset = Person.objects.filter(id=pk)
        if l_form.is_valid():
            l_form.save()
            messages.success(request, f'your image have beed added, good job!')
    else:
        l_form = PersonImageForm()
    return render(request, 'moments/add.html', {'form' : l_form, 'cato' : cato, 'pk' : pk})


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

class EventImageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = EventImage
    fields = ['event', 'image', 'story']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        event_image = self.get_object()
        if self.request.user == event_image.event.author:
            return True
        return False

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/moments/event'
    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
            return True
        return False

class EventImageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = EventImage
    success_url = '/moments/event'

    def test_func(self):
        event_image = self.get_object()
        if self.request.user == event_image.event.author:
            return True
        return False

class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'moments/event_home.html'
    context_object_name = 'events'
    ordering = ['date_created']
    paginate_by = 10

@login_required
def event_detail_view(request, pk, *args, **kwargs):
    event = get_object_or_404(Event, id = pk)
    photos = EventImage.objects.filter(event=event)
    return render(request, 'moments/event_detail.html', {
        'event' : event,
        'photos' : photos
        })

@login_required
def event_image_detail_view(request, pk, *args, **kwargs):
    info = get_object_or_404(EventImage, id = pk)
    photo = EventImage.objects.filter(id=pk)
    return render(request, 'moments/eventimage_detail.html', {
        'info' : info,
        'photos' : photo
    })

def add_event(request, cato, pk, *args, **kwargs):
    if request.method =='POST':
        l_form = EventImageForm(request.POST, request.FILES)
        l_form.fields['event'].queryset = Event.objects.filter(id=pk)
        if l_form.is_valid():
            l_form.save()
            messages.success(request, f'your image have beed added, good job!')
    else:
        l_form = EventImageForm()
    return render(request, 'moments/add.html', {'form' : l_form, 'cato' : cato, 'pk' : pk})


@login_required
def search(request):
    q = request.GET.get('que')
    error_msg = ''

    if not q:
        error_msg = '没有找到关联图片'
        return render(request, 'client/errors.html', {'error_msg': error_msg})

    image_list1 = CollectionImage.objects.filter(story__icontains=q)
    image_list2 = EventImage.objects.filter(story__icontains=q)
    image_list3 = PersonImage.objects.filter(story__icontains=q)

    return render(request, 'moments/results.html', {'error_msg': error_msg,
                                               'collection_image': image_list1,
                                               'event_image': image_list2,
                                               'person_image': image_list3})
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
