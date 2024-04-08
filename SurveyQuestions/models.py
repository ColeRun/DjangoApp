from django.db import models
from django.contrib.auth.models import User
  

class Survey(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Question(models.Model):
    TYPE_CHOICES = (
        ('text', 'Text'),
        ('radio', 'multiple choice'),
        ('checkbox', 'All That Apply'),
    )
    text = models.CharField(max_length=200)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    type = models.CharField(max_length=8, choices=TYPE_CHOICES, default='text')


class Option(models.Model):
    text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)