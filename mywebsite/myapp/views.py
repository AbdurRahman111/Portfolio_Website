from django.shortcuts import render, redirect
from .models import Contact_Us_Form
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'index.html')

def submit_contact_us_form(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')

    var_Contact_Us = Contact_Us_Form(Name=name, Email=email, Subject=subject, Message=message)
    var_Contact_Us.save()
    messages.success(request, 'Message Has Sent Successfully !!')
    return redirect('/')