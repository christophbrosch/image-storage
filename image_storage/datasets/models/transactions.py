from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from ..models import Image


# Create your models here.
class TimeableModel(models.Model):
    class Meta:
        abstract = True
    
    created_at = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

class Transaction(TimeableModel):
    dataset = models.ForeignKey("datasets.Dataset", on_delete=models.CASCADE)
    class meta:
        abstract = True

class ImageTransaction(Transaction):
    images = models.ManyToManyField(Image)

@receiver(signal=pre_delete, sender=ImageTransaction)
def image_transaction_pre_delete_handler(sender, instance, **kwargs):
    """Deletes images that belong to the Imagetransaction instance"""
    
    for image in instance.images.all():
        image.delete()

class AnnotationTransaction(Transaction):
    annotations = models.ManyToManyField('datasets.Annotation')

@receiver(signal=pre_delete, sender=AnnotationTransaction)
def annotation_transaction_pre_delete_handler(sender, instance, **kwargs):
    """Deletes images that belong to the Imagetransaction instance"""
    
    for annotation in instance.annotations.all():
        annotation.delete()