from django.urls import path
from seamknock_rest.models import UserDetail,Geofence
from seamknock_rest import views
from rest_framework import routers

urlpatterns = [
       path('registerUser/',views.UView.as_view(), name='ep1'),
       path('registerGeofence/', views.Geo_fence_View.as_view(), name='ep2'),
       path('accessGeofence/',views.Geo_fence_View.as_view(), name='ep3'),
       path('sknock/',views.Geo_fence_View.as_view(), name='ep3'),

]