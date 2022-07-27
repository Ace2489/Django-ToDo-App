from . import views
from django.urls import path

urlpatterns = [path('', views.getTasks, name = 'tasks'),
               path('<int:pk>',views.getTaskDetails, name = 'details'),
               path('create',views.createTask, name = 'create'),
               path('update/<int:pk>',views.updateTask, name = 'update'),
               path('delete/<int:pk>',views.deleteTask, name = 'delete'),
               path('logout', views.logout_user, name = 'logout') 
                ]