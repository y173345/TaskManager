from pyexpat import model
from statistics import mode
from django.db import models
import markdown
from django.utils import timezone

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    issue_date = models.DateField('issue date', default=timezone.now(), null=False, blank=False)
    # complete_date = models.DateField()
    deadline = models.DateField()
    is_done = models.BooleanField(default=False, blank=False)   
    description = models.TextField(blank=True, null=True)
    # tag = models.ManyToManyField(Tag)

    def markdown_to_html(self):
        md = markdown.Markdown(
            extensions=['extra', 'admonition', 'sane_lists', 'toc', 'markdown_checklist.extension'])
        html = md.convert(self.detail)

        return html
