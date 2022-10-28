from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def index(request):
    json_object = {"slackUsername" : "toyman", "backend" : True, "age" : 26, "bio" : "Taking it a step at a time, no stopping"} 

    return JsonResponse(json_object)