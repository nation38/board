from django.urls import path
from . import views

app_name = "book"

urlpatterns = [

    path('',views.index,name="index"),
    path('create/',views.create,name="create"), 
    path('remove/<bpk>',views.remove,name="remove"), 

]