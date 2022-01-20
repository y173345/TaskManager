from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=128)
    issue_date = models.DateTimeField('issue date')
    complete_date = models.DateTimeField()
    deadline = models.DateField()
    is_finished = models.BooleanField(default=False)   