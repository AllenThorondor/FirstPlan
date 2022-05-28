from django import forms
from .models import Post, PostImage


class PostImageForm(forms.ModelForm):

    class Meta:
        model = PostImage
        fields = ['post', 'story', 'image' ]

    post = forms.ModelChoiceField(queryset=Post.objects.order_by('-date_posted'))
