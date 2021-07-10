from django.shortcuts import render
from django.views.generic import DetailView

from ...models import Image
# Create your views here.

class DetailView(DetailView):
    model = Image
    template_name = "images/detail.html"