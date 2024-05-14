# views.py: take responsibility to accept request and send response

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.

def members(request):
    
    # example 3
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers':mymembers,
    }

    return HttpResponse(template.render(context, request))
    # example2
    #template = loader.get_template('myfirst.html')
    #return HttpResponse(template.render())
    
    # example1
    #return HttpResponse("Hello world!")

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
            'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],
        'firstname': 'Linux',
    }
    return HttpResponse(template.render(context,request))
