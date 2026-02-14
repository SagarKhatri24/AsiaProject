from django.shortcuts import render,redirect
from .models import *

#def indexView(self):

# Create your views here.
def indexView(request):
    if request.session.has_key('sessionName'):
        name = request.session["sessionName"]
    else:
        name = ""
    print(name)
    return render(request,'index.html',{"sName":name})

def aboutView(request):
    return render(request,'aboutus.html')

def signupView(request):

    if request.method == "POST":
        nameForm = request.POST["name"]
        emailForm =request.POST["email"]
        contactForm = request.POST["contact"]
        passwordField = request.POST["password"]
        confirmpasswordField = request.POST["confirmpassword"]
        genderField = request.POST["gender"]
        if passwordField == confirmpasswordField:
            #checkData = UserModel.objects.filter(email=emailForm) | UserModel.objects.filter(contact=contactForm)
            #print(checkData)
            #if len(checkData) > 0:
            #    return render(request,"signup.html",{"SignupError":"Users Already Exists"})
            checkData = UserModel.objects.filter(email=emailForm)
            checkContactData = UserModel.objects.filter(contact=contactForm)
            if len(checkData) > 0:
                return render(request,"signup.html",{"SignupError":"Email Already Exists"})
            elif len(checkContactData)>0:
                return render(request,"signup.html",{"SignupError":"Contact No. Already Exists"})
            else :
                userModel = UserModel()
                userModel.name = nameForm
                userModel.email = emailForm
                userModel.contact = contactForm
                userModel.password = passwordField
                userModel.gender = genderField

                userModel.save()
                #print("Signup Successfully")
                return redirect("loginName")
        else:
            return render(request,"signup.html",{"PasswordError":"Password Does Not Match"})
    return render(request,"signup.html")

def loginView(request):
    if request.method == "POST":
        emailForm =request.POST["email"]
        passwordField = request.POST["password"]
        checkData = UserModel.objects.filter(email=emailForm) & UserModel.objects.filter(password=passwordField)
        print(checkData)
        if len(checkData) > 0:
            userId = checkData[0].pk
            name = checkData[0].name
            email = checkData[0].email
            contact = checkData[0].contact
            password = checkData[0].password
            gender = checkData[0].gender

            request.session["sessionId"] = userId
            request.session["sessionName"] = name
            request.session["sessionEmail"] = email
            request.session["sessionContact"] = contact
            request.session["sessionPassword"] = password
            request.session["sessionGender"] = gender

            print(userId,name,email,contact,password,gender)
            return redirect("indexName")
        else :
            return render(request,"login.html",{"Message":"Login Unsuccessfully"})
    return render(request,"login.html")

def logoutView(request):
    request.session.clear()
    #request.session["sessionId"] = ""
    #request.session["sessionName"] = ""
    #request.session["sessionEmail"] = ""

    return render(request,"index.html")