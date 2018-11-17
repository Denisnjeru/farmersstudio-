from django.shortcuts import render
import requests
# Create your views here.
def pay():{
    
access_token = "LAKkBFK3q31PHpu6WVPmoIKANHnx"
#access_token = "LAKkBFK3q31PHpu6WVPmoIKANhnx"
api_url = "http://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
headers = {"Authorization": "Bearer %s" % access_token}
request = { "ShortCode": " ",
    "ResponseType": " ",
    "ConfirmationURL": "http://ip_address:port/confirmation",
    "ValidationURL": "http://ip_address:port/validation_url"}

response = requests.post(api_url, json = request, headers=headers)

print (response.text)
}