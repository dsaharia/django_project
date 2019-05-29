from django.http import HttpResponse

def home(requests):
    return HttpResponse('WELCOME HOME')