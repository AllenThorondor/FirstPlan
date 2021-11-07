from django import forms
from .models import Lane, Flash


class FlashForm(forms.ModelForm):

    lane = Lane.id
    class Meta:
        model = Flash
        fields = ['lane', 'story', 'picture' ]
"""
class FlashHookForm(forms.ModelForm):

    class Meta:
        model = Lane
        field = ['flight_num']
"""
