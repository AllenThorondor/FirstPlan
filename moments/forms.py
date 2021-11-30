from django import forms
from .models import (
    Collection,
    CollectionImage,
    Person,
    PersonImage,
    Event,
    EventImage)


class CollectionImageForm(forms.ModelForm):

    collection = Collection.id
    class Meta:
        model = CollectionImage
        fields = ['collection', 'image', 'story']

class PersonImageForm(forms.ModelForm):

    person = Person.id
    class Meta:
        model = PersonImage
        fields = ['person', 'image', 'story']

class EventImageForm(forms.ModelForm):

    event = Event.id
    class Meta:
        model = EventImage
        fields = ['event', 'image', 'story']
