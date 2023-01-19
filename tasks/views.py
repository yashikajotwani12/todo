from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        task = Task(title=title)
        task.save()
        return redirect('task_list')
    return render(request, 'task_form.html')

def task_complete(request, pk):
    task = Task.objects.get(pk=pk)
    task.completed = True
    task.save()
    return redirect('task_list')

def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('task_list')