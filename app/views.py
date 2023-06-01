from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def thor(request):
    return HttpResponse('<h2>THis is first view function of app1</h2>')
