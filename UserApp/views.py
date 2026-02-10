from django.shortcuts import render
from .models import *

#def indexView(self):

# Create your views here.
def indexView(request):
    return render(request,'index.html')

def aboutView(request):
    return render(request,'aboutus.html')

def signupView(request):

    if request.method == "POST":
        nameForm = request.POST["name"]
        emailForm =request.POST["email"]
        contactForm = request.POST["contact"]
        passwordField = request.POST["password"]
        genderField = request.POST["gender"]

        userModel = UserModel()
        userModel.name = nameForm
        userModel.email = emailForm
        userModel.contact = contactForm
        userModel.password = passwordField
        userModel.gender = genderField

        userModel.save()

        #return render(request,"login.html")

    return render(request,"signup.html")