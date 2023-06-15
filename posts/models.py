from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Post(models.Model):
    title = models.CharField(
        _("Blog Title"), max_length=250,
        null=False, blank=False
    )
    body = RichTextUploadingField()
    created_At = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title