from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import CreateView, FormView

# Create your views here.
from .forms import DriverForm, VehicleForm
from .models import Drivers, Vehicles

def adminHome(request):
    return render(request, 'adminhome.html')

def adminNotice(request):
    return render(request, 'adminnotice.html')

def adminEditnotice(request):
    return render(request, 'admineditnotice.html')

def adminUserCost(request):
    return render(request, 'adminusercost.html')

def adminUserRequest(request):
    return render(request, 'adminuserrequest.html')

def adminVehicle(request):
    return render(request, 'adminvehicle.html')

class addVehiclesView(FormView):
    model = Vehicles
    form_class = VehicleForm
    template_name = 'adminaddvehicle.html'
    success_url = 'AdminHome'
def adminAddvehicle(request):
     return render(request, 'adminaddvehicle.html')
def adminDriver(request):
    return render(request, 'admindriver.html')
class addDriverView(FormView):
    model = Drivers
    form_class = DriverForm
    template_name = 'adminadddriver.html'
    success_url = 'AdminHome'
def adminAdddriver(request):
     return render(request, 'adminadddriver.html')
# def requisitionform(request):
#     return render(request, 'userrequisition.html')

# def mycost(request):
#     return render(request, 'usermyCost.html')
