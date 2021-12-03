from django.shortcuts import render, redirect
from .models import Book

# Create your views here.

def index(request):
    b= request.user.book_set.all()


    context = {
        "blist" : b
    }

    return render(request,"book/index.html",context)

def create(request):


    if request.method == "POST":
        inpo =  request.POST.get("inpo")
        if inpo:
            inpo = True
        else:
            inpo = False
        name = request.POST.get("name")
        url = request.POST.get("url")
        co = request.POST.get("comment")
        Book(user = request.user, site_name = name,site_url = url, comment = co,impo=inpo).save()
        return redirect("book:index")



    return render(request,"book/create.html")

def remove(request,bpk):

    Book.objects.get(id=bpk).delete()

    return redirect("book:index")