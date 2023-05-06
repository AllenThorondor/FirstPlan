from django import forms
from .models import Company, CompanyUpdate


class CompanyUpdateForm(forms.ModelForm):

    class Meta:
        model = CompanyUpdate
        fields = ['story', 'company']
