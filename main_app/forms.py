from django.forms import ModelForm
from .models import Show

class ShowForm(ModelForm):
  class Meta:
    model = Show
    fields = ['date', 'time']