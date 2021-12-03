from django.shortcuts import render
import pdfplumber

def plum_daldal(filename):
    with pdfplumber.open(filename) as pdf:
        a =""
        for i in pdf.pages:
            page = i
            a = a + page.extract_text()
        return a

def index(request):
    context = {}
    if request.method == "POST":
        pre = request.FILES.get("pdf","")
        a = plum_daldal(pre)
        context.update({
            "A" : a
        })


    return render(request,"pdf/index.html",context)