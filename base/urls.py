from . import views
from django.urls import path

urlpatterns = [path('task', views.TaskList.as_view(), name = 'tasks'),
               path('task/<int:pk>',views.TaskDetails.as_view(), name = 'details'),
               path('task/create',views.TaskCreate.as_view(), name = 'create'),
               path('task/update/<int:pk>',views.updateTask, name = 'update'),
               path('task/delete/<int:pk>',views.deleteTask, name = 'delete') 
                ]