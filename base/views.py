from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth import logout
from .forms import TaskForm
from .models import Task


# Create your views here.
def getTasks(request):
    Tasks = Task.objects.all()
    return render(request, 'base/task_list.html', {'task_list':Tasks})

def getTaskDetails(request, pk):
    task = Task.objectsw.get(id = pk)
    return render(request, 'base/task_detail.html', {'task':task})


def createTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('tasks'))
    else:
        form = TaskForm()
    context = {'form':form}
    return render(request, 'base/task_form.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id = pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save() 
            return redirect(reverse('tasks'))
    return render(request, 'base/task_form.html', {'form':form})


def deleteTask(request, pk):
    task = Task.objects.get(id = pk)
    if request.method == 'POST':
        task.delete()
        return redirect(reverse('tasks'))
    return render(request, 'base/task_confirm_delete.html', {'task':task})

def logout_user(request):
    logout(request)
    return redirect(reverse('tasks'))