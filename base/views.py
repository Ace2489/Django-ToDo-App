from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import Task

# Create your views here.
class TaskList(ListView):
    model = Task

def getTasks(request):
    objects = Task.objects.all()
    return render(request, 'tasks.html', {'Tasks':objects})