from django import forms
from .models import Lane, Flash


class FlashForm(forms.ModelForm):

    class Meta:
        model = Flash
        fields = ['lane', 'story', 'picture' ]

    lane = forms.ModelChoiceField(queryset=Lane.objects.order_by('-takeoff_time'))
