from django.shortcuts import render
from django.http import  HttpResponseRedirect
from django.urls import reverse
from .models import Task

def index(request):
    # get all task lists from database to show on index page.
    task_list = Task.objects.all
    context = {'task_list': task_list}
    return render(request, 'lists/index.html', context)

def AddNewTask(request):
    # if text input isn't empty then save new one into database.
    if request.POST.get('task'):
        task = Task()
        task.task_text = request.POST.get('task')
        task.save()
        # After saved successful, redisplay to update tasks.
        return HttpResponseRedirect(reverse('index'))
 
