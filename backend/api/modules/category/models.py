from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    name = models.CharField(max_length=50)
    descr = models.CharField(max_length=350)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)