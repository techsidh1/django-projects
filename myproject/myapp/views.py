from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Create your views here.

def home(request):
    tasks = Task.objects.filter(completed=False).order_by("-created_at")
    completed_tasks = Task.objects.filter(completed=True)
    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks
    }
    return render(request, 'home.html',  context)


def create_task(request):
    task = request.POST['task'] 
    Task.objects.create(task=task)
    return redirect('home')


def done_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed= True 
    task.save()
    return redirect('home')


def undone_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed= False 
    task.save()
    return redirect('home')


def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        updated_task = request.POST['task']
        get_task.task = updated_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'task': get_task
        }
        return render(request, 'edit.html', context)

def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('home')