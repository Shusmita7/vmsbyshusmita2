from django.shortcuts import render
from django.shortcuts import redirect
# from django.views.generic import CreateView, FormView

# Create your views here.
# from .forms import DriverForm, VehicleForm
# from .models import Drivers, Vehicles

def subadminHome(request):
    return render(request, 'adminhome.html')

def subadminNotice(request):
    return render(request, 'subadminnotice.html')

def subadminEditnotice(request):
    return render(request, 'subadmineditnotice.html')

def subadminUserCost(request):
    return render(request, 'subadminusercost.html')

def subadminUserRequest(request):
    return render(request, 'subadminuserrequest.html')

def subadminVehicle(request):
    return render(request, 'subadminvehicle.html')

def subadminDriver(request):
    return render(request, 'subadmindriver.html')
