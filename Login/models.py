from django.db import models

# Create a model for organizations that use the survey, including the organization name and a description of the organization and an appropriate email address for the organization.
class Organization(models.Model):
    organization_name = models.CharField(max_length=100)
    organization_description = models.CharField(max_length=1000)
    organization_email = models.EmailField(max_length=100)


    