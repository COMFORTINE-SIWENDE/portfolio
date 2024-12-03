from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Portfolio(models.Model):
    experience = models.CharField(max_length=150)
    exp_path = models.URLField()
    
    skills = models.CharField(max_length=150)
    skill_path = models.URLField()
    
    projects = models.CharField(max_length=150)
    project_path = models.URLField()
    
    
