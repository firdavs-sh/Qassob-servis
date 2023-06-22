from multiprocessing import context
from django.shortcuts import render

from main.models import Mol, Mt, Ot, Qoy, Quyon, Register, Tovuq, Tuya

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


def menu (request):
    data=Qoy.objects.all()
    data1=Mol.objects.all()
    data2=Tuya.objects.all()
    data3=Quyon.objects.all()
    data4=Tovuq.objects.all()
    data5=Ot.objects.all()
    context={
        'data':data,
        'data1':data1,
        'data2':data2,
        'data3':data3,
        'data4':data4,
        'data5':data5,
        
    }
    return render (request,"menu.html",context)


def news (request):
    return render (request,"news.html")

def newsd (request):
    return render (request,"newsd.html")