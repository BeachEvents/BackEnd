from rest_framework import response 
from rest_framework.decorators import api_view
from django.shortcuts import HttpResponse
from .processing import processTime
import requests
import json
import time


@api_view(['GET'])
def getEvents(request):
    res = requests.get(f"https://csulb.campuslabs.com/engage/api/discovery/event/search?endsAfter={processTime()}&status=Approved&take&query")
    return response.Response(res.json()['value'])

@api_view(['GET'])
def getOrgs(request):
    res = requests.get(f"https://csulb.campuslabs.com/engage/api/discovery/event/search?endsAfter={processTime()}&orderByField=endsOn&orderByDirection=ascending&status=Approved&take=1000000000&query")
    return response.Response(res.json()['value'])

@api_view(['GET'])
def getOrgEvents(request):
    pass
# @api_view(['GET'])
# def getTime():
#     x = "asdf"
#     print(f"{processTime()}asd",x)



# getTime()
