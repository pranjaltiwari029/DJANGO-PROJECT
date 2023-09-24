from django.shortcuts import render,redirect
from .models import Task
from django.http import HttpResponse
# Create your views here.
def home(request):
    tasks=Task.objects.filter(is_completed=False).order_by('updated_at')
    
    completed_tasks=Task.objects.filter(is_completed=True)
    context={
        'tasks':tasks,
        'completed_tasks':completed_tasks,
    }
    
    # print(tasks)
    return render(request,'home-todo.html',context)

def addTask(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect("home")