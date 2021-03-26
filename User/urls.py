from django.urls import path
from user import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name = 'Home'),
    path('notice/', views.notice, name = 'Notice'),
    path('requisition/', views.requisitionform, name = 'Requisition'),
    path('history/', views.mycost, name = 'MyCost'),
    # path('', views. , name = ''),
    # path('', views. , name = ''),
    
]