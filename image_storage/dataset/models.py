from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Dataset(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

class Image(models.Model):
    dataset = models.OneToOneField(Dataset, on_delete=models.CASCADE)
