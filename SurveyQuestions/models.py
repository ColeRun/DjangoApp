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
        survey = models.ForeignKey(Survey, related_name='questions', on_delete=models.CASCADE)
        type = models.CharField(max_length=8, choices=TYPE_CHOICES, default='text')
    
class Option(models.Model):
        text = models.CharField(max_length=200)
        question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()