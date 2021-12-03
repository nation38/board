from django.shortcuts import redirect, render
from django.utils import timezone
from .models import Board, Reply
from django.core.paginator import Paginator
# Create your views here.

def likey(request, bpk):
    b = Board.objects.get(id=bpk)
    b.likey.add(request.user)
    return redirect("board:read",bpk=bpk)

def unlikey(request,bpk):
    b =Board.objects.get(id=bpk)
    b.likey.remove(request.user)
    return redirect("board:read",bpk=bpk)



def create_reply(request,bpk):

    com = request.POST.get("comment")
    if com:
        b = Board.objects.get(id=bpk)
        rep = request.user.username
        Reply(sub=b,replyer=rep,comment=com).save()
    return redirect("board:read",bpk=bpk)

def remove_reply(request, bpk, rpk):

    r = Reply.objects.get(id=rpk)
    if r.replyer != request.user.username:
        return render(request,"error/forbiden.html")

    r.delete()
    return redirect("board:read", bpk=bpk)



def index(request):
    a = Board.objects.all()
    kw = request.GET.get("kw", "")
    cate = request.GET.get("cate", "")
    if kw:
        if cate == "1":
            a = Board.objects.filter(subject__contains=kw)
        elif cate == "2":
            a = Board.objects.filter(writer__contains=kw)
        elif cate == "3":
            a = Board.objects.filter(content__contains=kw)
        else:
            a = Board.objects.all()
    else:
        a= Board.objects.all()
    
    a = a.order_by("-pubdate")
    page = request.GET.get("page",1)
    pag = Paginator(a, 10)
    obj = pag.get_page(page)

    
    context={
        "B" : obj,
        "cate" : cate,
        "kw" : kw
    }
    return render(request,'board/index.html',context)

def create(request):
    if request.method == "POST":
        su = request.POST.get("subject")
        wr = request.user.username
        co = request.POST.get("content")
        Board(subject = su, writer = wr, content=co, pubdate=timezone.now()).save()
        return redirect('board:index')
    return render(request,'board/create.html')

def read(request,bpk):
    a = Board.objects.get(id=bpk)
    r = a.reply_set.all()
    context = {
        "B" : a,
        "R" : r
    }
    return render(request, 'board/read.html',context)

def update(request,bpk):

    a = Board.objects.get(id=bpk)

    if request.user.username != a.writer:
        return render(request,"error/forbidden.html")
    if request.method == "POST":
        su = request.POST.get("subject")
        co = request.POST.get("content")
        a.subject = su
        a.content = co
        a.save()
        return redirect("board:read",bpk=bpk)
    context = {
        "B" : a
    }
    return render(request,'board/update.html', context)

def read_delete(request,bpk):
    a = Board.objects.get(id=bpk)
    if request.user.username != a.writer:
        return render(request,"error/forbidden.html")
    a.delete()
    return redirect("board:index")
