from django.shortcuts import render
import googletrans
from googletrans import Translator

# Create your views here.

def trans(a,b,c):
    text = a
 
    translator = Translator()
    trans = translator.translate(text, src=b, dest=c)
    return(trans.text)

    # 'en': 'english',    
    # 'ko': 'korean',    
    # 'el': 'greek',    
    # 'ja': 'japanese',   
    # 'it': 'italian',



def index(request):

    context ={}

    if request.method == "POST":
        before = request.POST.get("before","")
        form = request.POST.get("from","")
        to = request.POST.get("to","")
        if before:
            if form:
                if to:
                    if form == "ko":
                        src = "ko"
                    elif form == "en":
                        src = "en"
                    elif form == "it":
                        src = "it"
                    elif form == "ja":
                        src = "ja"
                    elif form == "el":
                        src = "el"
                    if to == "ko":
                        dest = "ko"
                    elif to == "en":
                        dest = "en"
                    elif to == "it":
                        dest = "it"
                    elif to == "ja":
                        dest = "ja"
                    elif to == "el":
                        dest = "el"
                    a = trans(before,src,dest)
                    context.update({"A":a, "from":src, "to":dest, "won":before})
                    


    return render(request,"trans/index.html",context)