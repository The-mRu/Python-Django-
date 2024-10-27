from typing import Any
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length= 200)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea) # widget for it is a text field

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@example.com'):
            raise forms.ValidationError('Email is not from "@example.com" domain.')
        return email