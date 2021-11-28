from django import forms
from .models import Collection, CollectionImage


class CollectionImageForm(forms.ModelForm):

    collection = Collection.id
    class Meta:
        model = CollectionImage
        fields = ['collection', 'image', 'story']
