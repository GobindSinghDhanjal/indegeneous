from django import views
from django.http import HttpResponse
from django.shortcuts import render

from asgard.models import Object

# Create your views here.

def index(request):
    objects = Object.get_all_objects()

    data={}
    data['objects'] = objects

    print(data)
    return render (request, 'index.html', data)
