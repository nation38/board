from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'acc/index.html')
def signup(request):
    if request.method == "POST":
        un = request.POST.get("username")
        if not User.objects.filter(username=un):            
            pw = request.POST.get("password")
            ni = request.POST.get("nickname")
            co = request.POST.get("comment")
            pi = request.FILES.get("pics")
            User.objects.create_user(username=un, password=pw, nickname=ni, comment=co, pic=pi)
            messages.success(request,"계정 생성 성공")
            return redirect("acc:login")
        else:
            messages.info(request,"이미 존재하는 이름입니다.")
            


    return render(request,"acc/signup.html")

def userlogin(request):
    if request.method == "POST":
        un = request.POST.get("username")
        pw = request.POST.get("password")
        user = authenticate(username=un, password=pw)
        if user:
            login(request, user)
            messages.success(request,"로그인 성공.")
        else:
            messages.error(request,"아이디나 비밀번호가 틀립니다.")
        return redirect("acc:index")
    return render(request,"acc/login.html")

def userlogout(request):
    logout(request)
    messages.info(request,"로그아웃 완료")
    return redirect("acc:index")

def profile(request):
    return render(request,"acc/profile.html")

def update(request):
    if request.method == "POST":
        user = request.user
        
        pw = request.POST.get("password")
        ni = request.POST.get("nickname")
        co = request.POST.get("comment")
        pi = request.FILES.get("pics")
        if pw:
            user.set_password(pw)
        user.nickname = ni
        user.comment = co
        if pi:
            user.pic.delete()
            user.pic = pi
        user.save()
        login(request, user)
        messages.info(request,"정보가 성공적으로 수정됨")
        return redirect("acc:profile")
    return render(request,"acc/update.html")

def user_delete(request):
    request.user.delete()
    return redirect("acc:index")