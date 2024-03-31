from seamknock_rest.models import UserDetail, Geofence
from rest_framework import serializers

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = ['emailId','api_key','api_secret','created']

class GeofenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geofence
        fields = ['lock_id','latitude','longitude','geofence_radius','created']        

