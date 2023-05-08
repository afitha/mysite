from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def prohome(request): 
    datasample=loader.get_template('prohome.html')
    data={}  
    response=datasample.render(data,request)
    return HttpResponse(response)


from .models import userinfo
def userinfosave(req):
    usr= userinfo(
        name = req.POST['na'],
        mail= req.POST['em'],
        password = req.POST['ps'],
        phone = req.POST['ph'],
    )
    usr.save()
    return HttpResponse("user created!!")


    

 
    
    