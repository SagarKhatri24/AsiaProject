from django.shortcuts import render

# Create your views here.
def indexViewVendor(request):
    return render(request,"indexNew.html")