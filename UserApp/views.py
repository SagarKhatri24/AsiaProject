from django.shortcuts import render

#def indexView(self):

# Create your views here.
def indexView(request):
    return render(request,'index.html')

def aboutView(request):
    return render(request,'aboutus.html')