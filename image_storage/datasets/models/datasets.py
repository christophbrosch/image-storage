from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class TimeableModel(models.Model):
    class Meta:
        abstract = True
    
    created_at = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

class Dataset(TimeableModel):
    ANNOTATION_FORMAT_CHOICES = (
        ('pascal_voc', 'Pascal VOC'),
        ('coco', 'COCO'),
        ('yolo', 'Yolo')
    )
    name = models.CharField(max_length=16)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE, db_column='owner')
    description = models.CharField(max_length=64, default='None')
    annotation_file_format = models.CharField(max_length=32, choices=ANNOTATION_FORMAT_CHOICES)
    labels = ArrayField(models.CharField(max_length=255, blank=True), size=64)

class Label(models.Model):
    models.CharField(primary_key=True, max_length=50)

