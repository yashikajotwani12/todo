from django.urls import path
from .views import task_list, task_create, task_complete, task_delete

urlpatterns = [
    path('', task_list, name='task_list'),
    path('add/', task_create, name='task_create'),
    path('complete/<int:pk>/', task_complete, name='task_complete'),
    path('delete/<int:pk>/', task_delete, name='task_delete')
]
