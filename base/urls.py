from . import views
from django.urls import path

urlpatterns = [path('', views.TaskList.as_view(), name = 'tasks'),
               path('<int:pk>',views.TaskDetails.as_view(), name = 'details'),
               path('create',views.TaskCreate.as_view(), name = 'create') 
                ]