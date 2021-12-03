from django.shortcuts import redirect, render
from .models import Topic, Choice
from django.utils import timezone
from django.contrib import messages


# Create your views here.

def create(request):

    sub = request.POST.get("subject")
    if sub:
        con = request.POST.get("content")
        name = request.POST.getlist("name")
        com = request.POST.getlist("comment")
        pic = request.FILES.getlist("pic")
        t = Topic(subject=sub,writer=request.user,pubdate=timezone.now(),content=con)
        if len(name)>1 and len(pic)>1:
            t.save()
            for i,j,k in zip(name,com,pic):
                Choice(subject=t,name=i,comment=j,pic=k).save()
            messages.success(request,"투표 생성 성공")
            return redirect("vote:index")

    return render(request,"vote/create.html")
    



def index(request):

    t= Topic.objects.all()
    t = t.order_by("-pubdate")
    context={
        "tlist" : t

    }

    return render(request,"vote/index.html",context)

def detail(request,tpk):
    t = Topic.objects.get(id=tpk)
    c = t.choice_set.all()
    context={
        "to" : t,
        "clist" : c
    }
    return render(request,"vote/detail.html",context)

def vote(request,tpk):
    t = Topic.objects.get(id=tpk)
    t.voter.add(request.user)
    cpk = request.POST.get("choice")
    c = Choice.objects.get(id=cpk)
    c.choicer.add(request.user)
    return redirect("vote:detail",tpk=tpk)

def cancel(request,tpk):
    t = Topic.objects.get(id=tpk)
    t.voter.remove(request.user)
    clist = t.choice_set.all()
    for i in clist:
        if request.user in i.choicer.all():
            i.choicer.remove(request.user)
    return redirect("vote:detail",tpk=tpk)