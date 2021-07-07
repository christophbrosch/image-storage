from django.db.models.signals import post_delete, pre_delete
from django.dispatch import receiver
from .models import ImageTransaction

@receiver(pre_delete, sender=ImageTransaction)
def image_transaction_pre_delete_handler(sender, **kwargs):
    pass