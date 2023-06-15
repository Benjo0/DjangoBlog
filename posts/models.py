from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    created_At = models.DateTimeField(default=datetime.now, blank=True)
  