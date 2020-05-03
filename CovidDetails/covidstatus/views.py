from django.http import HttpResponse
from django.template import loader
import requests
import json
x = requests.get("https://www.mohfw.gov.in/data/datanew.json")
x1=x.text
covid_data=json.loads(x1)

def homepage(req):
    template = loader.get_template('index.html')
    data = {'states': covid_data}
    res = template.render(data,req)
    return HttpResponse(res)

