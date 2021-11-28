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
from .models import Collection, CollectionImage
from .forms import CollectionImageForm
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
                'collections': Collection.objects.all(),
              }
    return render(request, 'moments/index.html', context)

def shop(request, pk, *args, **kwargs):
    collection = get_object_or_404(Collection, id = pk)
    photos = CollectionImage.objects.filter(collection=collection)
    context = {
                'collection' : collection,
                'photos' : photos
    }
    return render(request, 'moments/shop.html', context)

class CollectionListView(LoginRequiredMixin, ListView):
    model = Collection
    template_name = 'moments/home.html'
    context_object_name = 'collections'
    ordering = ['-date_created']
    paginate_by = 10

@login_required
def detail_view(request, pk, *args, **kwargs):
    collection = get_object_or_404(Collection, id = pk)
    photos = CollectionImage.objects.filter(collection=collection)
    return render(request, 'moments/collection_detail.html', {
        'collection' : collection,
        'photos' : photos
    })
"""
class LaneDetailView(LoginRequiredMixin, DetailView):
    model = Lane

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = LaneImage.objects.filter(lane=lane)
        context['flashes'] = Flash.objects.filter(lane=lane)
        return context

"""



class CollectionCreateView(LoginRequiredMixin, CreateView):
    model = Collection
    fields = ['collection_name', 'collection_num', 'discription', 'note', 'cover_image']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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


def add(request, *args, **kwargs):
    if request.method =='POST':
        l_form = CollectionImageForm(request.POST, request.FILES)
        if l_form.is_valid():
            l_form.save()
            messages.success(request, f'your image have beed added, good job!')
    else:
        l_form = CollectionImageForm()
    return render(request, 'moments/add.html', {'form' : l_form})


class CollectionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Collection
    success_url = '/moments/home'
    def test_func(self):
        collection = self.get_object()
        if self.request.user == collection.author:
            return True
        return False
