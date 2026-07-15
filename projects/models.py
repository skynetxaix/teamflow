from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    project_name=models.CharField(max_length=100)
    project_desc=models.CharField(max_length=500)
    project_own=models.ForeignKey(User,on_delete=models.CASCADE)