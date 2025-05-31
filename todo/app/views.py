from django.shortcuts import render
from .models import*
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request,'home.html')

def add_todo(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        desc=request.POST.get('desc')
        todo=Todo(title=title,desc=desc)
        todo.save()
        return  HttpResponseRedirect(reverse('list'))
    return render(request,'add_todo.html')

def list(request):
    todo=Todo.objects.all()
    return render(request,'list.html',{'todo':todo})

def update(request,pk):
    todo=Todo.objects.get(pk=pk)
    if request.method =='POST':
        title=request.POST.get('title')
        desc=request.POST.get('desc')
        todo.title=title
        todo.desc=desc
        todo.save()
        return  HttpResponseRedirect(reverse('list'))
    return render(request,'add_todo.html',{'todo':todo})
def delete(request,pk):
     todo=Todo.objects.get(pk=pk)
     if request.method =='POST':
         todo.delete()
         return  HttpResponseRedirect(reverse('list'))
     return render(request,'delete.html',{'todo':todo})

        


