from django.shortcuts import render

from ...models import Image

def expand(request, pk):
    images = Image.objects.filter(dataset__id = pk)[:12]
    return render(request, 'images/htmx/bar.html', context={'pk': pk, 'images': images, 'expand': False})

def collapse(request, pk):
    images = Image.objects.filter(dataset__id = pk)[:6]
    return render(request, 'images/htmx/bar.html', context={'pk': pk, 'images': images, 'expand': True})