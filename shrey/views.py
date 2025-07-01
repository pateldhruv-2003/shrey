from django.shortcuts import render
from .models import student,product
# Create your views here.

def index(request):
    return render(request,"index.html") 

def showstudentlist(request):
    stu = student.objects.all()
    return render(request,'showstudentlist.html',{'student':stu})

def showproductlist(request):
    pro= product.objects.all()
    return render(request,'showproductlist.html',{'product':pro})
    
