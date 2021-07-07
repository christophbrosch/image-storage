from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TimeableModel(models.Model):
    class Meta:
        abstract = True
    
    created_at = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

class Dataset(TimeableModel):
    name = models.CharField(max_length=16)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE, db_column='owner')
    description = models.CharField(max_length=64, default='None')