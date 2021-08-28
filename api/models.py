from django.db import models


# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=150)
    page = models.IntegerField(0)
