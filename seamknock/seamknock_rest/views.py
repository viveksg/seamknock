from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from seamknock_rest.models import UserDetail, Geofence
from seamknock_rest.serializers import UserDetailSerializer, GeofenceSerializer
from rest_framework import status
from seamknock_rest.seamconstants import Constants
from seamknock_rest.utils import Utils

class UView(APIView):
    def post(self,request,format=None):
        vemailId = request.POST[Constants.CONSTANT_EMAILID]
        utils = Utils()
        api_data = utils.generate_api_data(vemailId)
        data = {"emailId":vemailId,"api_key":api_data[Constants.CONSTANT_API_KEY],"api_secret":api_data[Constants.CONSTANT_API_SECRET]}
        user_serializer = UserDetailSerializer(data=data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status = 201)    
        return JsonResponse(user_serializer.data, status = 400) 


class Geo_fence_View(APIView):    

    def validate_credentials(api_key,api_secret,email_id):
        return True
    
    def post(self,request,format = None):
        email_id = request.POST[Constants.CONSTANT_EMAILID]
        api_key = request.POST[Constants.CONSTANT_API_KEY]
        request_type = request.POST[Constants.CONSTANT_REQUEST_TYPE]
        user_obj = UserDetail.objects.filter(emailId=email_id)
        if user_obj.count() > 0:
            print(user_obj[0].api_secret)
            api_secret = user_obj[0].api_secret
            utils = Utils()
            if utils.authenticate_api(email_id,api_key,api_secret):
                    latitude = request.POST[Constants.CONSTANT_LATITUDE]
                    longitude = request.POST[Constants.CONSTANT_LONGITUDE]
                    request_type = request.POST[Constants.CONSTANT_REQUEST_TYPE]
                    print("request_type = "+ str(request_type))
                    print(int(request_type) == Constants.REQUEST_CREATE_GEOFENCE)
                    if int(request_type) == Constants.REQUEST_CREATE_GEOFENCE:
                            lock_id = request.POST[Constants.CONSTANT_LOCKID]
                            radius = request.POST[Constants.CONSTANT_RADIUS]
                            data = {
                                "lock_id":lock_id,
                                "latitude":utils.toRadians(float(latitude)),
                                "longitude":utils.toRadians(float(longitude)),
                                "geofence_radius":radius
                                 }
                            geofence_serializer = GeofenceSerializer(data=data)
                            if geofence_serializer.is_valid():
                                geofence_serializer.save()
                                return JsonResponse(geofence_serializer.data, status = 201)    
                            return JsonResponse({"status":"cant create geofence record"}, status = 400) 
                    elif int(request_type) == Constants.REQUEST_ACCESS_GEOFENCE:  
                            query = utils.prepare_geofence_query(latitude,longitude)
                            geofence_objs = Geofence.objects.raw(query)
                            gfence_serializer = GeofenceSerializer(geofence_objs,many=True)
                            if gfence_serializer.data.count >0:
                                return JsonResponse(gfence_serializer.data,status=201)
                            return JsonResponse({"status":"cant access geofence record"}, status = 400) 
                    return JsonResponse({"status":"API authentication failed"}, status = 400) 
        return JsonResponse({"status":"Unable to fetch user record"}, status = 400)    
    
    def get(self,request,format = None):
        geofence_serializer = GeofenceSerializer.objects.all()

class KnockView(APIView):
    def post(self,request, format = None):
        pass