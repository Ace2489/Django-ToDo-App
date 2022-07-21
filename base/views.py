from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Task

# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name = 'task_list'


def getTasks(request):
    Tasks = Task.objects.all()
    return render(request, 'tasks.html', {'Tasks':Tasks})


class TaskDetails(DetailView):
    model = Task
    context_object_name = 'task'

def getTaskDetails(request, pk):
    task = Task.objects.get(id = pk)
    return render(request, 'task_detail.html', {'task':task})