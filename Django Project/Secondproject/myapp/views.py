from django.shortcuts import render
import random

# Create your views here.
n=1
def index(request):
    return render(request,'index.html',{'name':'Hitesh'})

def about(request):
    n={'num':random.randint(1111,9999)}
    return render(request,'about.html',n)

def contact(request):
    global n
    n+=1 #n=n+1
    return render(request,'contact.html',{'n':n})