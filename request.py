#Importing libraries 
import requests;
import json
import hashlib
from retry.api import retry_call


#api end-points
res = requests.get('http://0.0.0.0:8888/auth')
print(res.headers)
token = res.headers['Badsec-Authentication-Token']
print(token)


def get_checksum(token, path_to_request):
    value = hashlib.sha256(token+path_to_request).hexdigest()
    return value
    ##hello world



valuechecksum = get_checksum(token,'/users')
print(valuechecksum)
    

