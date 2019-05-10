from django.shortcuts import render
import requests # for getting the API response
# # Create your views here.
from django.http import HttpResponse

def github(requests):
    return HttpResponse('Hello Git')
    # def github(requests):
    #     user = {}