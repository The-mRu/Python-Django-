from typing import Any
from django import forms
from book.models import Book 

class ContactForm(forms.Form):
    name = forms.CharField(max_length= 200)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea) # widget for it is a text field

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@example.com'):
            raise forms.ValidationError('Email is not from "@example.com" domain.')
        return email

# Task 3: Create ModelForm for Book model
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'publication_date', 'author', 'price', 'publisher']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError('Price must be positive.')
        return price    