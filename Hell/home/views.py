from django import http
from django.http.response import JsonResponse
from django.shortcuts import render,HttpResponse
from home.models import user,fav

# Create your views here.
def home(request):
    return HttpResponse("hello")
 
def add(request,fname,lname,email):
    r = user.objects.create(fname=fname,lname = lname,email=email)
    r.save()
    context = {
       "name":r.fname,
        "email":r.email
        }
    return render(request,"test.html",context)

def getuser(request,id):
    us =user.objects.get(id=id)
    q=fav.objects.filter(id =id)
    favs  =[]
    for v in q:
        favs.append(v.name)
    res = {
        "fname":us.fname,
        "lname":us.lname,
        "email":us.email,
        "favs":favs
    }
    return HttpResponse(JsonResponse(res))

def favs(request,id ,name): 
    favs = fav.objects.create(uid = id,name = name)
    favs.save()
    return HttpResponse(favs.name) 


def rmfavs(request,id,name):
    f = fav.objects.get(id = id,name = name)
    fs = fav(f.id)
    fs.delete()
    return HttpResponse("deleted")