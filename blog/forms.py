from django import forms
from .models import Post, PostImage


class PostImageForm(forms.ModelForm):

    post = Post.id
    class Meta:
        model = PostImage
        fields = ['post', 'story', 'image' ]
