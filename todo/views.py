from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
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
    template_name = 'todo/contact.html'
    form_class = RegisterForm
