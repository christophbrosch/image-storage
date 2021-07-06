import io
from copy import deepcopy

from django.db import models
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.storage import default_storage
from PIL import Image as PIL_IMAGE
from django.db.models.fields.related import ForeignKey
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

class ImageManager(models.Manager):
    def create(self, file, *args, **kwargs):
        """ Overwritten to upload the image to default_storage and create a thumbnail which is also uploaded to default_storage """

        # copying the file becuase apparently something inside S3Boto3Storage is closing the file for now reason
        # TODO: Smart things
        file_copy = SimpleUploadedFile(file.name, file.read(), file.content_type)
        try:
            # Upload image
            path = default_storage.save(file.name, file)
        # TODO: Custom Exceptions
        except Exception as e:
            raise type(e)(f'Could not upload {file.name}')
        else:
            try:
                # Create image object
                object = super().create(path = path, dataset = kwargs['dataset'])
            except Exception as e:
                try:
                    # Delete image in case image object creation failed
                    default_storage.delete(path)
                except:
                    # TODO: try again later
                    raise type(e)(f'Internal error, could not upload {file.name}')
            else:
                # Create the thumbnail
                pil_image = PIL_IMAGE.open(file_copy)
                factor = pil_image.width / 250
                pil_image.thumbnail((250, pil_image.height / factor)) # TODO: Not hardcode size
                buffer = io.BytesIO()
                pil_image.save(buffer, 'JPEG')
                buffer.seek(0)
                try:
                    default_storage.save(object.thumbnail_path, ContentFile(buffer.read()))
                except Exception as e:
                    pass # log error and try uploading again later
        return object

class Image(TimeableModel):
    path = models.CharField(max_length=255)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)

    @property
    def extension(self):
        return self.path.split('.')[-1]

    @property
    def thumbnail_path(self):
        return self.path.replace(f'.{self.extension}', f'_thumbnail.{self.extension}')

    objects = ImageManager()

class Transaction(TimeableModel):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    class meta:
        abstract = True

class ImageTransaction(Transaction):
    images = models.ManyToManyField(Image)