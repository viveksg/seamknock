from seamknock_rest.seamconstants import Constants
import random
import hashlib
import math
import pyqrcode
import png
from pyqrcode import QRCode
import io

class Utils:
    __DEFAULT_SEED_LENGTH = 255
    __RADIUS = 6371
    __GEOFENCE_TABLE_NAME = "seamknock_rest_geofence"
    __COL_NAME_LATITUDE = "latitude"
    __COL_NAME_LONGITUDE = "longitude"
    __COL_NAME_RADIUS = "geofence_radius"
    def __generate_seed(self, seed_length):
        chrstore =  []
        for i in range(10):
            chrstore.append(Constants.ASCII_ZERO_START + i)
        for i in range(26):
            chrstore.append(Constants.ASCII_A_START + i)
        for i in range(26):
            chrstore.append(Constants.ASCII_SMALL_A_START + i)
        total_len = 62
        seed_str = ""
        random.seed()
        for i in range(total_len):
            random_val = random.randint(10000, 1<< 63 -1)
            seed_str = seed_str+ str(chr(chrstore[random_val%total_len]))
        print(seed_str)   
        print('\n') 
        return seed_str      

    def generate_api_data(self,emailId):
        #generate a sudo random number as a seed value
        api_hash = hashlib.sha256()
        secret_hash = hashlib.sha256()
        seed = self.__generate_seed(self.__DEFAULT_SEED_LENGTH)
        api_base_str = emailId + seed
        api_hash.update((api_base_str).encode("utf-8"))
        api_key = api_hash.hexdigest()
        hashed_base_str = api_key + emailId
        secret_hash.update((hashed_base_str).encode("utf-8"))
        hashed_api_key = secret_hash.hexdigest()
        return {Constants.CONSTANT_API_KEY:api_key,Constants.CONSTANT_API_SECRET:hashed_api_key}
    
    def authenticate_api(self,emailId,api_key,hashed_value):
        hashed_var = hashlib.sha256()
        base_str = api_key + emailId
        hashed_var.update(base_str.encode("utf-8"))
        hashed_key = hashed_var.hexdigest()
        return (hashed_value == hashed_key)
    
    def prepare_geofence_query(self,lat,lng):
        lat = self.toRadians(float(lat))
        lng = self.toRadians(float(lng))
        query = (f"SELECT * FROM {self.__GEOFENCE_TABLE_NAME} WHERE acos(sin({lat}) * sin({self.__COL_NAME_LATITUDE}) + cos({lat}) * cos({self.__COL_NAME_LATITUDE}) * cos({self.__COL_NAME_LONGITUDE} - ({lng}))) * {self.__RADIUS} <= {self.__COL_NAME_RADIUS}")
        return query

    def toRadians(self, val):
        return math.radians(val)
    
    def generateQRcode(self,strval):
        qrval=pyqrcode.create(strval)
        buffer = io.BytesIO()
        qrval.png(buffer)
        print(qrval.text())
        return buffer
   
    
