from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Dataset(models.Model):
    name = models.CharField(max_length=16)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE, db_column='owner')
    description = models.CharField(max_length=64, default='None')

class Image(models.Model):
    dataset = models.OneToOneField(Dataset, on_delete=models.CASCADE)
