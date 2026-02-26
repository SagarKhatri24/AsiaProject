from django.shortcuts import render,redirect
from .models import *

#def indexView(self):

def sessionData(request):
    if request.session.has_key('sessionName'):
        userId = request.session["sessionId"]
        name = request.session["sessionName"]
        email = request.session["sessionEmail"]
        contact = request.session["sessionContact"]
        password = request.session["sessionPassword"]
        gender =  request.session["sessionGender"]

        userData = {
            "id" : userId,
            "name" : name,
            "email" : email,
            "contact" : contact,
            "password" : password,
            "gender" : gender
        }
    else : 
        userData = {}
    return userData

# Create your views here.
def indexView(request):
    sData = sessionData(request)
    print(sData)
    if request.session.has_key('sessionName'):
        name = request.session["sessionName"]
    else:
        name = ""
    print(name)
    return render(request,'index.html',{"session":sData})

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
    sData = sessionData(request)
    if sData:
        request.session.clear()
        #request.session["sessionId"] = ""
        #request.session["sessionName"] = ""
        #request.session["sessionEmail"] = ""
        return redirect("indexName")
    else:
        return redirect("indexName")

def profileView(request):
    sData = sessionData(request)
    if sData:
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
                userModel = UserModel(pk=request.session["sessionId"])
                userModel.name = nameForm
                userModel.email = emailForm
                userModel.contact = contactForm
                userModel.password = passwordField
                userModel.gender = genderField
                userModel.save()

                request.session["sessionName"] = nameForm
                request.session["sessionEmail"] = emailForm
                request.session["sessionContact"] = contactForm
                request.session["sessionPassword"] = passwordField
                request.session["sessionGender"] = genderField

                #print("Signup Successfully")
                return redirect("profileName")
            else:
                return render(request,"profile.html",{"session":sData,"PasswordError":"Password Does Not Match"})
        return render(request,"profile.html",{"session":sData})
    else : 
        return redirect("indexName")