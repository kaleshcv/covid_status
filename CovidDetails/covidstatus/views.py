from django.http import HttpResponse
from django.template import loader
import requests
import json
from .models import Destination,Blog,Gallery



def covidstatus(req):
    x = requests.get("https://www.mohfw.gov.in/data/datanew.json")
    x1 = x.text
    covid_data = json.loads(x1)

    total=covid_data[38]

    statenumbers = [0, 4, 9, 11, 14, 16, 17, 20, 21, 28, 29, 31, 33, 35, 36]
    statewisedata = []

    for i in statenumbers:
        data = covid_data[i]

        statename = data['state_name']
        positive = data['new_positive']
        recovered = data['new_cured']
        death = data['new_death']
        recovery_percentage = int(recovered) / int(positive) * 100
        rec_per = int(recovery_percentage)
        rp = str(rec_per) + '%'

        dp = str(int(int(death) / int(positive) * 100)) + '%'
        x = dict(state=statename, Total=positive, cured=recovered, death=death, rp=rp, dp=dp)
        statewisedata.append(x)

    template = loader.get_template('covidstatus.html')
    data = {'states': statewisedata,'total':total}
    res = template.render(data,req)
    return HttpResponse(res)




def homepage(req):
    x = requests.get("https://www.mohfw.gov.in/data/datanew.json")
    x1 = x.text
    covid_data = json.loads(x1)

    total = covid_data[38]

    statenumbers = [16, 17, 33,21,31,9]
    statewisedata = []

    for i in statenumbers:
        data = covid_data[i]

        statename = data['state_name']
        positive = data['new_positive']
        recovered = data['new_cured']
        death = data['new_death']
        recovery_percentage = int(recovered) / int(positive) * 100
        rec_per = int(recovery_percentage)
        rp = str(rec_per) + '%'

        dp = str(int(int(death) / int(positive) * 100)) + '%'
        x = dict(state=statename, Total=positive, cured=recovered, death=death, rp=rp, dp=dp)
        statewisedata.append(x)

    template = loader.get_template('index.html')
    all_dest = Destination.objects.all()[:4]
    all_blogs=Blog.objects.all().order_by('blog_date').reverse()[:3]
    data={'destinations':all_dest,'blogs':all_blogs,'states':statewisedata,'total':total}
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
    all_blogs=Blog.objects.all().order_by('blog_date').reverse()
    data={'blogs':all_blogs}
    res = template.render(data,req)
    return HttpResponse(res)

def contact(req):
    template = loader.get_template('contact.html')

    data={}
    res = template.render(data,req)
    return HttpResponse(res)

def gallery(req):
    template = loader.get_template('gallery.html')
    images=Gallery.objects.all().order_by('img_date').reverse()
    data={'images':images}
    res = template.render(data,req)
    return HttpResponse(res)

