from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

from taggit.models import TaggedItem

class Food(models.Model):
    name = models.CharField(max_length=20)

    tags = TaggableManager()
