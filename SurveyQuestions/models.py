from django.db import models
from django.contrib.auth.models import User
  

class Survey(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Question(models.Model):
    text = models.CharField(max_length=200)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

class Answer(models.Model):
    text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)