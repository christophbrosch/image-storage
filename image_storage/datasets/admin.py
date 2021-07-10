from django.contrib import admin

from .models.datasets import Dataset
from .models.images import Image
from .models.transactions import ImageTransaction

# Register your models here.
admin.site.register(Dataset)
admin.site.register(Image)
admin.site.register(ImageTransaction)