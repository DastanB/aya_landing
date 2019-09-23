from django import forms

class ContactForm(forms.Form):
    fio = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=13)
