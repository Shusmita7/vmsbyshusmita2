from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def notice(request):
    return render(request, 'notice.html')

def requisitionform(request):
    return render(request, 'requisitionForm.html')

def mycost(request):
    return render(request, 'myCost.html')

