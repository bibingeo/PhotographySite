from django.db import models
from django import forms
from django.forms import ModelForm

from .models import contactinfo ,booknow


class ContactForm(ModelForm):
    class Meta:
        model = contactinfo
        fields ={'first_name','email','phone','comment'}
        widgets = {'first_name' : forms.TextInput(attrs={'class':'form-control',
                                                    'placeholder':'enter your first name'}),
                   'email': forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'enter your email'}),
                   'phone': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'enter your phone number'}),
                   'comment': forms.Textarea(attrs={'class': 'form-control',
                                                   'placeholder': 'enter your comments'}),

                }



class BooknowForm(ModelForm):
    class Meta:
        model = booknow
        fields ={'name','email','mobile','city','state','comment'}
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'enter your first name'}),
                   'email': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder': 'enter your email'}),
                   'mobile': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder': 'enter your mobile number'}),
                   'city': forms.TextInput(attrs={'class': 'form-control',
                                                    'placeholder': 'city'}),
                   'state': forms.TextInput(attrs={'class': 'form-control',
                                                    'placeholder': 'state '}),

                   'comment': forms.Textarea(attrs={'class': 'form-control',
                                                     'placeholder': 'enter your comments'}),

                   }


