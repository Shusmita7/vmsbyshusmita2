# from django.db import models
# from django.utils import timezone
# from django.contrib.auth.models import User

# #  Create your models here.

# class Requisitionsinfo(models.Model):
#    # requisitionId_no = models.IntegerField(default=primary_key =True)
#    # serial_no = models.IntegerField()
#    date = models.DateTimeField(default=timezone.now)

#    author = models.ForeignKey(User, on_delete=models.CASCADE)
#    designation = models.CharField(max_length = 100)
#    department = models.CharField(max_length = 100)
#    journey_purpose = models.CharField(max_length=33)
#    journey_date = models.DateTimeField(auto_now_add=True)
#    vehicle_type = models.CharField(max_length = 100)
#    destination = models.CharField(max_length = 300)
#    departure_time = models.TimeField()
#    return_time = models.TimeField()
#    journey_details = models.TextField(max_length = 400)