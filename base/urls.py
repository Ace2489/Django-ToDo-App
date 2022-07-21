from . import views
from django.urls import path

urlpatterns = [path('', views.getTasks, name = 'tasks'),
               path('<int:pk>',views.getTaskDetails, name = 'details') 
                ]