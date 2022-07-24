from . import views
from django.urls import path

urlpatterns = [path('task', views.getTasks, name = 'tasks'),
               path('task/<int:pk>',views.getTaskDetails, name = 'details'),
               path('task/create',views.createTask, name = 'create'),
               path('task/update/<int:pk>',views.updateTask, name = 'update'),
               path('task/delete/<int:pk>',views.deleteTask, name = 'delete') 
                ]