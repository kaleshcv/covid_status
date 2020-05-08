from django.http import HttpResponse
from django.template import loader
import requests
import json
from .models import Destination,Blog



def covidstatus(req):
    x = requests.get("https://www.mohfw.gov.in/data/datanew.json")
    x1 = x.text
    covid_data = json.loads(x1)
    template = loader.get_template('covidstatus.html')
    data = {'states': covid_data}
    res = template.render(data,req)
    return HttpResponse(res)


def homepage(req):
    template = loader.get_template('index1.html')
    all_dest = Destination.objects.all()
    all_blogs=Blog.objects.all()
    data={'destinations':all_dest,'blogs':all_blogs}
    res = template.render(data,req)
    return HttpResponse(res)

def destinations(req):
    template = loader.get_template('destinations.html')
    all_dest = Destination.objects.all()
    data={'destinations':all_dest}
    res = template.render(data,req)
    return HttpResponse(res)

def blogs(req):
    template = loader.get_template('blogs.html')
    all_blogs=Blog.objects.all()
    data={'blogs':all_blogs}
    res = template.render(data,req)
    return HttpResponse(res)

def destinationsdetails(req):
    template = loader.get_template('destinationdetails.html')
    all_dest = Destination.objects.all()
    data={'destinations':all_dest}
    res = template.render(data,req)
    return HttpResponse(res)

def blogdetails(req):
    template = loader.get_template('blogdetails.html')
    all_blogs = Blog.objects.all()
    data = {'blogs': all_blogs}
    res = template.render(data,req)
    return HttpResponse(res)