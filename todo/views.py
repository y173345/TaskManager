from pydoc import resolve
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, resolve_url
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from .models import Task
from .forms import RegisterForm

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'todo_list'
    model = Task

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)

        keyword = self.request.GET.get('keyword')
        if keyword is not None:
            queryset = queryset.filter(title__contains=keyword)

        queryset = queryset.filter(issue_date__lte=timezone.now()).order_by("-issue_date")

        return queryset

class DetailView(generic.detail.DetailView):
    model = Task
    template_name = 'todo/detail.html'
    context_object_name = 'detail'


# def detail(request, todo_id):
#     return HttpResponse("You're looking at question %s." % todo_id)

# def results(request, todo_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % todo_id)

class RegisterFormView(generic.edit.CreateView):
    model = Task
    template_name = 'todo/register.html'
    context_object_name = 'register'
    form_class = RegisterForm
    success_url = reverse_lazy('todo:index')

    def get_success_url(self) -> str:
        messages.success(self.request, ('Your task is added!'))
        return resolve_url('todo:index')
