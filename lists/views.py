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

def DeleteTask(request):
    try:
        # get task is selected from radio input.
        selected_task = Task.objects.get(pk=request.POST['Task'])
    # if user didn't select and clicked 'Completed' button,
    # error massage will appear to notice.
    except (KeyError, Task.DoesNotExist):
        return render(request, 'lists/index.html', {
            'task_list': Task.objects.all,
            'error_message': "You didn't select a task.",
        })
    else:
        # user selected one, selected task is removed and reload page. 
        selected_task.delete()
        return HttpResponseRedirect(reverse('index'))
