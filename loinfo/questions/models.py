from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    category = models.CharField(max_length=50)
    ask = models.TextField()

    def __str__(self):
        return self.category

