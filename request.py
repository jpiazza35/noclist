#Importing libraries 
import requests
import json
import hashlib
from retry.api import retry_call

def get_checksum(token, path_to_request):
    value_to_string = token+path_to_request
    value = hashlib.sha256(value_to_string.encode('utf8')).hexdigest()
    return value


#api end-points
baseurl = 'http://0.0.0.0:8888'
res = requests.get(baseurl+'/auth')
print(res.headers)
token = res.headers['Badsec-Authentication-Token']
print("este es el token", type(token))

path = '/users'
valuechecksum = get_checksum(token,path)
print(valuechecksum)

##setting header    
headers = {'X-Request-Checksum': valuechecksum}
res = requests.get(baseurl+path, headers=headers)
print(res.body)

    





