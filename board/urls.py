from os import name
from django.urls import path
from . import views

app_name = "board"

urlpatterns = [
    path('',views.index, name="index"),
    path('create',views.create, name="create"),    
    path('read/<bpk>',views.read, name="read"),    
    path('update/<bpk>',views.update, name="update"),    
    path('delete/<bpk>',views.read_delete, name="delete"),   
    path('create_reply/<bpk>',views.create_reply, name="create_reply"),
    path('remove_reply/<bpk>/<rpk>',views.remove_reply, name="remove_reply"),
    path('likey/<bpk>',views.likey, name="likey"),
    path('unlikey/<bpk>',views.unlikey, name="unlikey")
]

