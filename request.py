#Importing libraries 
import requests
import json
import hashlib
from retry.api import retry_call


#api end-points
res = requests.get('http://0.0.0.0:8888/auth')
print(res.headers)
token = res.headers['Badsec-Authentication-Token']
print("este es el token", type(token))


def get_checksum(token, path_to_request):
    value_to_string = token+path_to_request
    value = hashlib.sha256(value_to_string.encode('utf8')).hexdigest()
    return value
    



valuechecksum = get_checksum(token,'/users')
print(valuechecksum)
    

