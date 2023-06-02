from django.shortcuts import render,redirect
from .forms import userForm
from .models import userdata

# Create your views here.
def index(request):
    if request.method=='POST':
        newuser=userForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Your data has been saved!")
        else:
            print(newuser.errors)
    return render(request,'index.html')

def showdata(request):
    data=userdata.objects.all()
    return render(request,'showdata.html',{'data':data})

def updatedata(request,id):
    stid=userdata.objects.get(id=id)
    if request.method=='POST':
        newuser=userForm(request.POST)
        if newuser.is_valid():
            newuser=userForm(request.POST,instance=stid)
            newuser.save()
            print("Your data has been updated!")
            return redirect('showdata')
        else:
            print(newuser.errors)
    return render(request,'updatedata.html',{'stid':userdata.objects.get(id=id)})

def deletedata(request,id):
    stid=userdata.objects.get(id=id)
    userdata.delete(stid)
    return redirect('showdata')
