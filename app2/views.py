from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def sky(request):
    return HttpResponse('<h1><marquee>sky in the fly</marquee></h1>')