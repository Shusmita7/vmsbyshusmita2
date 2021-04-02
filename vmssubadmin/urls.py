from django.urls import path
from vmssubadmin import views
urlpatterns = [
    path('', views.subadminHome, name = 'SubadminHome'),
    path('subnotice/', views.subadminNotice, name = 'SubadminNotice'),
    path('subnotice/editNotice/', views.subadminEditnotice, name ='subadminEditNotice'),
    path('subusercost/', views.subadminUserCost, name ='SubadminUserCost'),
    path('subrequest/', views.subadminUserRequest, name ='SubaminUserRequest'),
    path('subvehicle/', views.subadminVehicle, name ='SubadminVehicle'),
    path('subdriver/', views.subadminDriver, name ='SubadminDriver'),
]