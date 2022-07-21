from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import TaskForm
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

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    context_object_name = 'form'

def createTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('tasks'))
    else:
        form = TaskForm()
    context = {'form':form}
    return render(request, 'task_form.html', context)
