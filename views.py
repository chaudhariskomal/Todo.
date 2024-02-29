from django.shortcuts import render,HttpResponse,redirect
from todoapp.models import Task 

# Create your views here.
def home(request):
    return redirect('/display')

def display(request):
    # obj={'task':[{'id':1, 'name':'Exercise', 'time':'6 AM'},
    #              {'id':2, 'name':'Drink Water', 'time':'7 AM'},
    #              {'id':3, 'name':'Breckfast', 'time':'8 AM'}
    #              ]}
    obj=Task.objects.all()
    e={'task':obj}
    return render(request, 'task.html',e)

def remove(request,tid):
    obj=Task.objects.filter(id=tid)
    obj.delete()
    return redirect('/display')

def add(request):
    if request.method=='GET':
        return render(request,'addtask.html')
    else:
        print('Data Collected')
        nm=request.POST['name']
        time=request.POST['time']
        obj=Task.objects.create(name=nm, time=time)
        obj.save()
        return redirect('/display')

def edit(request,tid):
    if request.method=='GET':
        obj=Task.objects.filter(id=tid)
        return render(request,'edit.html',{'task':obj})
    else:
        print('Data Collected')
        nm=request.POST['name']
        time=request.POST['time']
        obj=Task.objects.filter(id=tid)
        obj.update(name=nm, time=time)
        return redirect('/display')

# def index(request):
#     return render(request,'index.html')
