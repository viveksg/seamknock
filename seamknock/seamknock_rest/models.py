from django.db import models

# Create your models here.
class UserDetail(models.Model):
    emailId = models.EmailField(max_length=200,primary_key=True)
    api_key = models.CharField(max_length=200)
    api_secret = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add = True)
 
    class Meta:
        ordering = ['created']

class Geofence(models.Model):
    lock_id = models.CharField(max_length=200,primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    geofence_radius = models.FloatField()
    created = models.DateTimeField(auto_now_add = True) 

    class Meta:
        ordering = ['created']       
    
    def select_geofence(self, lat, lng):
        pass