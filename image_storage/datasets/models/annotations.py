from django.db import models
from django.db import models
from django.core.files.storage import default_storage

class TimeableModel(models.Model):
    class Meta:
        abstract = True
    
    created_at = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

class AnnotationManager(models.Manager):
    def create(self, file, image, format, *args, **kwargs):
        try:
            # Upload annotation file
            path = default_storage.save(file.name, file)
        # TODO: Custom Exceptions
        except Exception as e:
            raise type(e)(f'Could not upload {file.name}')
        else:
            try:
                # Create annotation object
                object = super().create(path = path, image = image, format=format)
            except Exception as e:
                try:
                    # Delete annotation file in case annotation object creation failed
                    default_storage.delete(path)
                except:
                    # TODO: try again later
                    raise type(e)(f'Internal error, could not upload {file.name}')
            else:
                return object

class Annotation(TimeableModel):
    path = models.CharField(max_length=255)
    image = models.ForeignKey('datasets.Image', on_delete=models.CASCADE)
    format = models.CharField(max_length=32)
    
    objects = AnnotationManager()