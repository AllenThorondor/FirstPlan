from django import forms
from .models import Post, PostImage


class PostImageForm(forms.ModelForm):

    class Meta:
        model = PostImage
        fields = ['post', 'story', 'image' ]

    post = forms.ModelChoiceField(queryset=Post.objects.order_by("-date_posted"))

'''    def __init__(self, *args, **kwargs):
        post_id = kwargs.pop('id', None)
        super(PostImageForm, self).__init__(*args, **kwargs)

        if post_id:
            self.fields['post'].queryset = Post.objects.filter(id=post_id)'''
