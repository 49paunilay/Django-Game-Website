from django.shortcuts import render,HttpResponse
from .models import *

def home(request):
    catagories = Catagory.objects.all()
    images = Images.objects.all()
    context={
        'images':images,
        'catagories':catagories
    }
    return render(request,'index.html',context)

def catagory(request,cid):
    catagories = Catagory.objects.all()
    C=Catagory.objects.get(pk=cid)
    images = Images.objects.filter(catagory=C)
    context={
        'images':images,
        'catagories':catagories
    }
    return render(request,'index.html',context)