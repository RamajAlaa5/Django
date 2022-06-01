from django.contrib import admin
from django.urls import path, include
from .views import get_index,task_details,delete_task,edit_task,mark_as_done,create_task,add_task,update_task
app_name="todo"
urlpatterns=[
    path('index',get_index,name="index"),
    path('mark_as_done/<str:id>', mark_as_done, name="mark_as_done"), 
    path('create_task', create_task, name="create_task"),    
    path('add_task', add_task, name="add_task"),
    path('task_details/<str:id>',task_details,name="task_details"),
    path('delete_task/<str:id>',delete_task,name="delete_task"),
    path('edit_task/<str:id>',edit_task,name="edit_task"),
    path('update_task',update_task,name="update_task"),    

]