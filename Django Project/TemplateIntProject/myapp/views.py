from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def couple(request):
    return render(request,'couple.html')

def gallery(request):
    return render(request,'gallery.html')