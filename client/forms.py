from django import forms
from .models import Company, CompanyUpdate


class CompanyUpdateForm(forms.ModelForm):

    class Meta:
        model = CompanyUpdate
        fields = ['company', 'story' ]

    company = forms.ModelChoiceField(queryset=Company.objects.order_by("-date_posted"))

'''    def __init__(self, *args, **kwargs):
        post_id = kwargs.pop('id', None)
        super(PostImageForm, self).__init__(*args, **kwargs)

        if post_id:
            self.fields['post'].queryset = Post.objects.filter(id=post_id)'''
