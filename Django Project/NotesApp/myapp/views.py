from django.shortcuts import render,redirect
from .forms import signupForm,updateForm,notesForm
from .models import userSignup
from django.contrib.auth import logout

# Create your views here.

def index(request):
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("Signup Successfully!")
                #return redirect('notes')
            else:
                print(newuser.errors)
        elif request.POST.get('login')=='login':

            unm=request.POST['username']
            pas=request.POST['password']

            uid=userSignup.objects.get(username=unm)
            print(uid.id)
            user=userSignup.objects.filter(username=unm,password=pas)
            if user:
                print("Login Successfully!")
                request.session['user']=unm
                request.session['userid']=uid.id
                return redirect('notes')
            else:
                print("Error!Login fail....")
    return render(request,'index.html')

def notes(request):
    user=request.session.get('user')
    if request.method=='POST':
        newnotes=notesForm(request.POST,request.FILES)
        if newnotes.is_valid():
            newnotes.save()
            print("Notes Submitted!")
        else:
            print(newnotes.errors)
    return render(request,'notes.html',{'user':user})

def profile(request):
    user=request.session.get('user')
    uid=request.session.get('userid')
    cuser=userSignup.objects.get(id=uid)
    if request.method=='POST':
        updateProfile=updateForm(request.POST,instance=cuser)
        if updateProfile.is_valid():
            updateProfile.save()
            print("Your profile has been updated!")
        else:
            print(updateProfile.errors)
    return render(request,'profile.html',{'user':user,'uid':cuser})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def userlogout(request):
    logout(request)
    return redirect('/')
