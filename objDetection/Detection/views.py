from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from email_validator import validate_email,EmailNotValidError
import requests
from django.conf import settings
from .models import Object
from .forms import MyModelForm
import os
from .far.untitled5 import detect_objects

objects = None


# Create your views here.
def index(request):
    q = {}
    if request.user.is_anonymous:
        q['user'] = False
    else:
        q['user'] = True
        q['username'] = request.user.username
    return  render(request,"index.html",q)

def loginUser(request):
    if request.method == 'GET':
        if 'login' in request.GET:
            return render(request,'login.html',{'q' : True})
        elif 'request' in request.GET:
            return render(request,'login.html',{'q' : False})
        else:
            return render(request,'login.html')
    
    elif request.method == 'POST':

        if 'confirm password' in request.POST:
            username = request.POST['username']
            email = request.POST['login']  # Assuming this is intended to be the email.
            password = request.POST['password']
            confirm_password = request.POST['confirm password']
            
            # Simple validation example
            if password == confirm_password and is_valid_email(email):
                # Create the user and log them in, etc.
                user = User.objects.create_user(username, email, password)
                user.save()
                
            else:
                # make error that user exists
                if is_valid_email(email):
                    return HttpResponse('Invalid email credentials')
                
                else:
                    return HttpResponse('Passwords dont match')
        else:
            # check if user is logged in    
            email = request.POST.get('email')
            password = request.POST.get('password')
            
        user = authenticate(email=email, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect("/dashboard")
        else:
            # No backend authenticated the credentials
            print(user)
            return render(request,'login.html')
        
        
        
def is_valid_email(email):
    try:
        # Validate.
        valid = validate_email(email)
        # Update with the normalized form.
        email = valid.email
        return True
    except EmailNotValidError as e:
        # Email is not valid, exception message is human-readable
        return False


def logoutUser(request):
    logout(request)
    return redirect('/login')


def contact(request):
    # if post request aarahi hai tau database mei store kardo
    q = {}
    if request.user.is_anonymous:
        q['user'] = False
    else:
        q['user'] = True
        q['username'] = request.user.username
    return render(request,'contact.html',q)


def user_dashboard(request):
    q = {}
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        q['user'] = True
        q['username'] = request.user.username
    l = request.user.reverse_relationship.all()

    
    if request.method == 'POST' and 'file' in request.FILES.keys():
        try:
            uploaded_file = request.FILES['file']
            obj = Object(image_location = uploaded_file,user = request.user)
            obj.save()        
            messages.success(request,'File uploaded')
        except Exception as e:
            print(e)
            messages.error(request, "Error uploading file: {}".format(e),extra_tags='danger')
    else:
        print("No file")
        
    q['data'] = []
    q['images'] = []
    for i in l:
        image_location = i.image_location
        dictionary = {"path" : image_location, "name" : os.path.basename(i.image_location.name.split('.')[0])}
        q['data'].append(dictionary)
    return render(request, "userhome.html", q)
    
def details(request,name = None):
    q={}
    print("details function")
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        q['user'] = True
        q['username'] = request.user.username
        
    if request.method == 'POST' and 'file' in request.FILES.keys():
        try:
            uploaded_file = request.FILES['file']
            handle_uploaded_file(uploaded_file)
            print("Hello i am here")
            detections, processed_image_path = detect_objects(uploaded_file.name)
            print("Hello I am there")
            q['detections'] = detections
            q['processed_image_path'] = processed_image_path
            messages.success(request,'File uploaded')
        except Exception as e:
            print(e)
            messages.error(request, "Error uploading file: {}".format(e),extra_tags='danger')
    else:
        print("No file")
        
    return render(request,"details.html",q)



def handle_uploaded_file(f):
    file = "Detection/far/" + f.name
    with open(file, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
