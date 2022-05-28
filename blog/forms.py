from django import forms
from .models import Post, PostImage


class PostImageForm(forms.ModelForm):

    class Meta:
        model = PostImage
        fields = ['post', 'story', 'image' ]

    post = forms.ChoiceField(choices=enumerate(Post.objects.order_by('-date_posted')))
