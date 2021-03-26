from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'userhome.html')

def notice(request):
    return render(request, 'usernotice.html')

def requisitionform(request):
    return render(request, 'userrequisition.html')

def mycost(request):
    return render(request, 'usermyCost.html')

