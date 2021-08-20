from django.db import models
from datetime import datetime
from tinymce.models  import HTMLField
# from ckeditor.fields import RichTextField



# Create your models here.
class Room(models.Model):
     name = models.CharField(max_length=1000)

class Message(models.Model):
    value = HTMLField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
