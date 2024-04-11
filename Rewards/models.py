from django.db import models

# Create your models here.

class Background(models.Model):
    background_name = models.CharField(max_length=100)
    background_description = models.CharField(max_length=1000)
    background_image = models.ImageField(upload_to='images/')

class Color(models.Model):
    color_name = models.CharField(max_length=100)
    color_value = models.CharField(max_length=100)