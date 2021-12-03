from django.urls import path, include
from . import views

app_name = "extra"


urlpatterns = [
    path('',views.index,name="index"),
]