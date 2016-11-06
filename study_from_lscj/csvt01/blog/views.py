from django.shortcuts import render
from django.template import loader , Context , Template
from django.http import HttpResponse
# Create your views here.
'''
def index(req):
    t = loader.get_template('index.html')
    c = Context({'uname':'wxh'})
    html = t.render(c)
    return HttpResponse(html)
'''
def index(req):
    t = loader.get_template('index.html')
    c = Context({'uname':'wxh'})
    return HttpResponse(t.render(c))

def index1(req):
    t = Template('<h1>hello {{uname}}</h1>')
    c = Context({'uname':'wdh'})
    return HttpResponse(t.render(c))