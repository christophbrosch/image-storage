from django.forms import ModelForm

from .models import Dataset

class CreateForm(ModelForm):
    class Meta:
        model = Dataset
        fields = ['name']