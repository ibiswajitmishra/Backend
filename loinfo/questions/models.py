from django.db import models

class Question(models.Model):
    author_name = models.CharField(max_length=50,default="Guest")
    category = models.CharField(max_length=50)
    ask = models.CharField(max_length=250)
    username = models.CharField(max_length=20,unique=True,null=True)
    date_created = models.DateTimeField(verbose_name='Date created',auto_now_add=True,null=True)
    date_updated = models.DateTimeField(verbose_name='Date updated',auto_now=True,null=True)

    def __str__(self):
        return self.username

