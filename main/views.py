from multiprocessing import context
from django.shortcuts import render

from main.models import  Mt, Register

# Create your views here.
def about (request):
    return render (request,"about.html")

def contact (request):
    x=''
    s=''
    sata=Mt.objects.all()

    try:
        ism=request.POST.get('ism')
        familiya=request.POST.get('familiya')
        email=request.POST.get('email')
        telefon=request.POST.get('telefon')
        xabar=request.POST.get('xabar')
        if ism is not "" and familiya is not "" and email is not "" and telefon is not "" and xabar is not "":
            sms=Register(ism=ism,Familiya=familiya,Email=email,telefon=telefon,taklif=xabar)
            if sms.save():
             s='Saqlandi'
        else:
                x="Fo'rmani to'liq to'ldiring  !!"
    except:
         x="Fo'rmani to'liq to'ldiring !"
    return render (request,"contact.html",{'x':x,'s':s,'sata':sata})

def index (request):
    return render (request,"index.html")




def news (request):
    return render (request,"news.html")

def newsd (request):
    return render (request,"newsd.html")