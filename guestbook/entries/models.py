from django.db import models
from django.utils import timezone

# Create your models here.
class Entries(models.Model):
    author = models.TextField()
    comment = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
