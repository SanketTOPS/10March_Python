from django.shortcuts import render,redirect
from .forms import signupForm
from .models import userSignup

# Create your views here.

def index(request):
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        user=userSignup.objects.filter(username=unm,password=pas)
        if user: #true
            print("Login successfull!")
            request.session['user']=unm #create a session
            return redirect('home')
        else:
            print("Error!Incorrect username or password.")
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully!")
            return redirect('/')
        else:
            print(newuser.errors)
    return render(request,'signup.html')

def home(request):
    user=request.session.get('user')
    return render(request,'home.html',{'user':user})