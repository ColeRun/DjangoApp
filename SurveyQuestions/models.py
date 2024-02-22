from django.db import models

# Create a model for surveys 
class Survey(models.Model):
    survey_name = models.CharField(max_length=100)
    survey_description = models.CharField(max_length=1000)
    survey_date = models.DateField()
    survey_question = models.CharField(max_length=1000)
    survey_answer = models.CharField(max_length=1000)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)
