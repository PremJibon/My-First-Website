from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        "variable":"ksafk"
    }
    
    return render(request,"index.html",context)
def about(request):
    return render(request,"about.html")
    #return HttpResponse("This is about page")
def services(request):
    return render(request,"services.html")
    #return HttpResponse("This is service page")
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('dsec')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your profile has been submited')
    return render(request,"contact.html")
    #return HttpResponse("This is contact page")
def action(request):
    return render(request,"action.html")
    #return HttpResponse("this is action page")
def game(request):
    return render(request,"game.html")
    #return HttpResponse("this is action page")
def bhubon(request):
    return render(request,"bhubon.html")
    #return HttpResponse("this is action page")
def card(request):
    return render(request,"card.html")
    #return HttpResponse("this is action page")    
def doodle(request):
    return render(request,"doodle.html")
    #return HttpResponse("This is about page")    
def pong(request):
    return render(request,"pong.html")
    #return HttpResponse("This is about page")    
def breakout(request):
    return render(request,"breakout.html")
    #return HttpResponse("This is about page")    
def snake(request):
    return render(request,"snake.html")
    #return HttpResponse("This is about page")    