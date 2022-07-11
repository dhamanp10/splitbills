# forms.py
from string import Template
from django.utils.safestring import mark_safe
from django import forms
from django.forms import DateInput
from splitbills import settings
from app.models.Group import Group
from app.models.Transaction import Transaction
from app.models.User import User


class PictureWidget(forms.widgets.Widget):
  def render(self, name, value, attrs=None, **kwargs):
    html = Template("""<img class="rounded-circle" src="$media$link" width="100" height="100" />""")
    return mark_safe(html.substitute(media=settings.MEDIA_URL, link=value))

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

class Edit_my_details(forms.ModelForm):

  class Meta:
    model = User
    fields = ['image']
