from django.db import models
from projects.models import Project
# Create your models here.


class Task (models.Model):
    STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('in_progress', 'In Progress'),
    ('done', 'Done'),
]
    task_name=models.CharField(max_length=100)
    task_status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')
    task_project=models.ForeignKey(Project,on_delete=(models.CASCADE))
