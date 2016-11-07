from django.shortcuts import render
from blog.models import ServerService
from django.shortcuts import render_to_response
def index(req):
    ser = ServerService.objects.all()
    return  render_to_response('index.html',{'ser':ser})
