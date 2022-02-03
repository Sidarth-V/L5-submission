from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from tasks.models import Task

def task_view(request):
  search_term = request.GET.get("search")
  current_tasks = Task.objects.filter(deleted=False).filter(completed=False)
  if search_term:
    current_tasks = current_tasks.filter(title__icontains=search_term)
  return render(request, "tasks.html", { "tasks": current_tasks})

def add_task_view(request):
  task_value = request.GET.get("task")
  Task(title = task_value).save()
  return HttpResponseRedirect("/tasks")

def delete_task_view(request, index):
  Task.objects.filter(id = index).update(deleted=True)
  return HttpResponseRedirect("/tasks")

def completed_tasks_view(request):
  completed_tasks = Task.objects.filter(completed=True)
  return render(request, "completed.html", { "tasks": completed_tasks})

def complete_task_view(request, index):
  Task.objects.filter(id = index).update(completed=True)
  return HttpResponseRedirect("/tasks")

def all_tasks_view(request):
  current_tasks = Task.objects.filter(deleted=False).filter(completed=False)
  completed_tasks = Task.objects.filter(completed=True)
  return render(request, "all_tasks.html", {"current": current_tasks, "completed": completed_tasks})
