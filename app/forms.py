# forms.py
from django import forms
from django.forms import DateInput

from app.models.Group import Group
from app.models.Transaction import Transaction

class Create_group(forms.ModelForm):

  class Meta:
    model = Group
    fields = ['name', 'image']


class Create_transaction(forms.ModelForm):

  class Meta:
    model = Transaction
    fields = ['title', 'description','image','date']
    widgets = {
      'date': DateInput(),
    }