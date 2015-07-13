# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from onesite.models import OneSiteDemo
# Create your views here.
def one_site_demo(request):
    name = 'one_site_demo'
    return render_to_response('onesitedemo_one.html', {'name': name})

def one_site_all(request):
    to = OneSiteDemo.objects.all()
    return render_to_response('onesitedemo_all.html', {'to': to})

