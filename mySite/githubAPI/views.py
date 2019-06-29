from django.shortcuts import render
import requests # for getting the API response
# # Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def github(request):
    if request.method == 'POST':
        return HttpResponse(request.POST['username'])
    return render(request, 'githubAPI/base.html')