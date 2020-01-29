from django.shortcuts import render
from .models import Task

def index(request):
    # get all task lists from database to show on index page.
    task_list = Task.objects.all
    context = {'task_list': task_list}
    return render(request, 'lists/index.html', context)
