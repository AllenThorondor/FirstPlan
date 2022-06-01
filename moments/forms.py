from django import forms
from .models import (
    Collection,
    CollectionImage,
    Person,
    PersonImage,
    Event,
    EventImage)


class CollectionImageForm(forms.ModelForm):

    class Meta:
        model = CollectionImage
        fields = ['collection', 'image', 'story']

    collection = forms.ModelChoiceField(queryset=Collection.objects.order_by('-date_created'))

class PersonImageForm(forms.ModelForm):

    class Meta:
        model = PersonImage
        fields = ['person', 'image', 'story']

    person = forms.ModelChoiceField(queryset=Person.objects.order_by('-date_created'))

class EventImageForm(forms.ModelForm):

    class Meta:
        model = EventImage
        fields = ['event', 'image', 'story']

    event = forms.ModelChoiceField(queryset=Event.objects.order_by('-date_created'))
