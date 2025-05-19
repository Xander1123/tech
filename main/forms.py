# forms.py
from django import forms
from .models import ContactMessage  # Yalnız lazım olan importları edirik

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
