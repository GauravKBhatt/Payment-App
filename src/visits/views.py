from django.shortcuts import render
from django.views import View
from .models import *

class HomeView(View):
    def get(self,request,*args,**kwargs):
        pagevisits=PageVisit.objects.filter(path=request.path)
        context={
            'name':"Home Page",
            'pagevisits':pagevisits.count()
        }
        PageVisit.objects.create(path=request.path)
        return render(request,'home.html',context)


