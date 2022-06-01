from pickle import FALSE, TRUE
from urllib import request
from django.shortcuts import render,redirect,reverse

# Create your views here.

my_todos = {
    '1': {
        'id': 1,
        'name': 'python',
        'priority': 2,
        'is_done': False
    },
    '2': {
        'id': 2,
        'name': 'php',
        'priority': 1,
        'is_done': True
    },
    '3': {
        'id': 3,
        'name': 'laravel',
        'priority': 3,
        'is_done': False
    },
    '4': {
        'id': 4,
        'name': 'java',
        'priority': 4,
        'is_done': False
    }
}

def get_index(request):
    return render(request,'index.html',context={'todo_list':my_todos})

def task_details(request,**kwargs):
    task_id=kwargs.get('id')
    task=my_todos.get(task_id)
    return render(request,'details.html',context={'task':task})

def delete_task(request,**kwargs):
    task_id=kwargs.get('id')
    my_todos.pop(task_id)
    return redirect(reverse("todo:index"))

    # return render(request,'index.html',context={'task':task})
    


def mark_as_done(request, **kwargs):
    task_id = kwargs.get('id')
    task = my_todos.get(task_id)
    task['is_done'] = True
    return redirect(reverse("todo:index"))

def create_task(request):
        return render(request,'add.html')
    
def add_task(request):
    task_id=request.POST.get('id')
    my_todos[task_id]={
        'name':request.POST.get('name'),
        'priority':request.POST.get('priority')
    } 
    task=my_todos.get(task_id)
    if(request.POST.get('status')==TRUE):
        task['is_done']=True
    else:
                task['is_done']=False
    return redirect(reverse("todo:index"))

def edit_task(request,**kwargs):
    task_id=kwargs.get('id')
    task=my_todos.get(task_id)
    return render(request,'edit.html',context={'task':task}) 
 
def update_task(request):
    task_id = request.POST.get('id')
    task = my_todos.get(task_id)
    task['name'] = request.POST.get('name')
    task['priority'] = request.POST.get('priority')
    if(request.POST.get('status') == "True"):
        task['is_done'] = True
    else:
        task['is_done'] = False
    return redirect(reverse("todo:index"))

        
        
    
   
            


    

           
