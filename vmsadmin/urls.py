from django.urls import path
from vmsadmin import views
urlpatterns = [
    path('', views.adminHome, name = 'AdminHome'),
    path('notice/', views.adminNotice, name = 'AdminNotice'),
    path('notice/editNotice/', views.adminEditnotice, name ='adminEditNotice'),
    path('usercost/', views.adminUserCost, name ='AdminUserCost'),
    path('request/', views.adminUserRequest, name ='AdminUserRequest'),
    path('vehicle/', views.adminVehicle, name ='AdminVehicle'),
    path('vehicle/addvehicle/', views.adminAddvehicle, name ='adminAddVehicle'),
    path('driver/', views.adminDriver, name ='AdminDriver'),
    path('driver/adddriver/', views.adminAdddriver, name ='adminAddDriver'),
]
