from django.shortcuts import render

# Create your views here.

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
def adminAddvehicle(request):
    return render(request, 'adminaddvehicle.html')
def adminDriver(request):
    return render(request, 'admindriver.html')
def adminAdddriver(request):
    return render(request, 'adminadddriver.html')
# def requisitionform(request):
#     return render(request, 'userrequisition.html')

# def mycost(request):
#     return render(request, 'usermyCost.html')
