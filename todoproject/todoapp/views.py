from django.shortcuts import render, redirect

from .forms import todoform
from .models import Task
from django.views.generic import ListView

# Create your views here.



def home(request):
    task1 = Task.objects.all()
    if request.method=="POST":
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,"home.html",{'task':task1})

def delete(request,id ):
    task=Task.objects.get(id=id)
    if request.method=="POST":
         task.delete()
         return redirect('/')
    return  render(request,'delete.html')
def update(request,id):
    task=Task.objects.get(id=id)
    f=todoform(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return  render(request,'edit.html',{'f':f,'task':task})

