from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Task


# Create your views here.
#Tasks
@login_required
def getTasks(request):
    Tasks = Task.objects.all().filter(User_id = request.user.id)
    return render(request, 'base/task_list.html', {'task_list':Tasks})


@login_required
def getTaskDetails(request, pk):
    task = Task.objects.get(id = pk)
    return render(request, 'base/task_detail.html', {'task':task})


@login_required
def createTask(request):
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('tasks'))
    else:
        form = TaskForm()
    context = {'form':form}
    return render(request, 'base/task_form.html', context)


@login_required
def updateTask(request, pk):
    task = Task.objects.get(id = pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save() 
            return redirect(reverse('tasks'))
    return render(request, 'base/task_form.html', {'form':form})


@login_required
def deleteTask(request, pk):
    task = Task.objects.get(id = pk)
    if request.method == 'POST':
        task.delete()
        return redirect(reverse('tasks'))
    return render(request, 'base/task_confirm_delete.html', {'task':task})



#USERS AND STUFF
@login_required
def logout_user(request):
    logout(request)
    return redirect(reverse('login'))

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request, 'base/signup.html', context)

def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username= username, password = password)
            login(request, user)
            return redirect('tasks')
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'base/login.html', context)

