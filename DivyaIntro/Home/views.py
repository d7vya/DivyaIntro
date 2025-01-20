from django.shortcuts import render
from Home.models import Contact
# Create your views here.
def home(request):
    return render(request,'homepage.html')
def projects(request):
    return render(request,'projects.html')

def about(request):
    return render(request,'about.html')


def contact(request):
    if request.method=="POST":
        contact= Contact(name=request.POST['name'],email=request.POST['email'],contact_no=request.POST['contact'])
        contact.reason= request.POST['reason']
        contact.save()
        context={'submit':True,'name':request.POST['name']}
        return render(request,'contact.html',context)
    
    return render(request,'contact.html')