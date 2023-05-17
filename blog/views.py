from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView)
from .models import Post, PostImage
from .forms import PostImageForm
from taggit.models import Tag


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'  #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        #user = get_object_or_404(User, username=self.kwargs.get('username'))
        #request.user
        return Post.objects.filter(author=self.request.user).order_by('-date_posted')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['common_tags'] = Post.tags.most_common()[:4]

        return context


class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/user_posts.html'  #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


@login_required
def post_detail_view(request, pk, *args, **kwargs):
    post = get_object_or_404(Post, id=pk)
    photos = PostImage.objects.filter(post=post)
    page = request.GET.get('page')

    return render(request, 'blog/post_detail.html', {
        'post' : post,
        'photos' : photos,
        'page' : page
    })


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html',{'title':'About'})

def tagged(request, pk):
    tag = get_object_or_404(Tag, id=pk)
    common_tags = Post.tags.most_common()[:4]

    posts = Post.objects.filter(author=request.user, tags=tag)

    context = {
        'tag':tag,
        'common_tags':common_tags,
        'posts':posts,
    }
    return render(request, 'blog/home.html', context)

@login_required
def add_post_image(request, pk, *args, **kwargs):

    if request.method == 'POST':
        l_form = PostImageForm(request.POST, request.FILES)
        l_form.fields['post'].queryset = Post.objects.filter(id=pk)

        if l_form.is_valid():
            l_form.save()
            messages.success(request, f'your image have beed added, good job!')
            return redirect('post-detail', pk=pk)
    else:
        l_form = PostImageForm()
    return render(request, 'blog/add.html', {'form' : l_form, 'pk' : pk})

class ImageAddView(LoginRequiredMixin, UserPassesTestMixin, FormView):
    form_class = PostImageForm
    template_name = 'blog/add.html'

    def test_func(self):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        if self.request.user == post.author:
            return True
        return False

    def form_valid(self, form):
        target_post = get_object_or_404(Post, pk=self.kwargs['pk'])
        update = form.save(commit=False)

        update.post = target_post
        update.save()

        self.success_url = target_post.get_absolute_url()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        target_company = get_object_or_404(Post, pk=self.kwargs['company_id'])

        return render(self.request, 'client/company_detail.html', {
            'form' : form,
            'company' : target_company,
            'update_list' : target_company.update_set.all()
        })
