from django.contrib import admin
from .models import Dataset, Image, ImageTransaction
# Register your models here.

admin.site.register(Dataset)
admin.site.register(Image)
admin.site.register(ImageTransaction)