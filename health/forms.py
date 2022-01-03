from django import forms
from .models import Record
from django.urls import reverse
import pytesseract
from PIL import Image, ImageDraw


class RecordForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = ['picture' ]
