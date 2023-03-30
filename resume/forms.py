from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=100)
    phone = forms.CharField(max_length=13)
    comment = forms.CharField(widget=forms.Textarea(attrs={'row': 3}))

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 2:
            raise ValidationError("Name length must be greater then 2")
        return name

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(phone) != 10:
            raise ValidationError("Phone number must be of 10 length")
        return phone