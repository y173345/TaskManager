from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Task

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        return Task.objects.filter(issue_date__lte=timezone.now()).order_by("-issue_date")[:10]


class DetailView(generic.detail.DetailView):
    model = Task
    template_name = 'todo/detail.html'
    context_object_name = 'detail'


# def detail(request, todo_id):
#     return HttpResponse("You're looking at question %s." % todo_id)

# def results(request, todo_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % todo_id)
