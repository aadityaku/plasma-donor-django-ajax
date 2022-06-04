from dataclasses import fields
from django.http import HttpResponse, JsonResponse
from dajaxice.utils import deserialize_form
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.shortcuts import redirect, render,HttpResponseRedirect
from django.views.generic import View,ListView,DetailView,UpdateView,CreateView
from .forms import *
from .models import *
from django.core import serializers
# Create your views here.
def donorStateWise():
    
    for i in State.objects.all():
        total=Donor.objects.filter(d_state=i).count
        if total:
            return total

class HomeView(ListView):
    model=Donor
    
    def get_context_data(self,*args,**kwargs):
        context=super(HomeView,self).get_context_data()
        context['states']=State.objects.all()
        context['donorCount']=Donor.objects.all().count()
        context['requesterCount']=Requester.objects.all().count()
        context['donor']=Donor.objects.all()
        context['city']=City.objects.all()
        context['sum'] = Donor.objects.filter().count()
        
        context['requester']=Requester.objects.all()
        return context
    
    


def insertDonor(r):
    donorform=DonorForm(r.POST or None)
    state=State.objects.all()
    city=City.objects.all()
    if r.method == "POST":
        
        if donorform.is_valid():
            
            d_name=donorform.cleaned_data.get('d_name')
            d_age=donorform.cleaned_data.get('d_age')
            d_gender=donorform.cleaned_data.get('d_gender')
            
            d_bloodGroup=donorform.cleaned_data.get('d_bloodGroup')
            d_covid_pos_date=donorform.cleaned_data.get('d_covid_pos_date')
            d_covid_neg_date=donorform.cleaned_data.get('d_covid_neg_date')
            d_state=r.POST["d_state"]
            a=State.objects.get(id=d_state)
            d_city=r.POST["d_city"]
            b=City.objects.get(id=d_city)
            donor=Donor.objects.create(d_name=d_name,d_age=d_age,d_gender=d_gender,d_bloodGroup=d_bloodGroup,d_covid_pos_date=d_covid_pos_date,
            d_covid_neg_date=d_covid_neg_date,d_state=a,d_city=b)
            donor.save()
            
            return redirect("homepage")
    else:
        return render(r,"data/donor_form.html",{"donor":donorform,"states":state,"cities":city})
def insertRequester(r):
    donorform=RequesterForm(r.POST or None)
    state=State.objects.all()
    city=City.objects.all()
    if r.method == "POST":
        
        if donorform.is_valid():
            
            d_name=donorform.cleaned_data.get('r_name')
            d_age=donorform.cleaned_data.get('r_age')
            d_gender=donorform.cleaned_data.get('r_gender')
            
            d_bloodGroup=donorform.cleaned_data.get('r_bloodGroup')
            d_covid_pos_date=donorform.cleaned_data.get('r_covid_pos_date')
            d_covid_neg_date=donorform.cleaned_data.get('r_covid_neg_date')
            d_state=r.POST['d_state']
            a=State.objects.get(id=d_state)
            d_city=r.POST['d_city']
            b=City.objects.get(id=d_city)
            donor=Requester(r_name=d_name,r_age=d_age,r_gender=d_gender,r_bloodGroup=d_bloodGroup,r_covid_pos_date=d_covid_pos_date,
            r_covid_neg_date=d_covid_neg_date,r_state=a,r_city=b)
            donor.save()
            
            return redirect("homepage")
    else:
        return render(r,"data/requester_form.html",{"requester":donorform,"states":state,"cities":city})


def donorView(r):
    state=State.objects.all()
    city=City.objects.all()
    data={"donors":Donor.objects.all(),"count":Donor.objects.all().count(),"states":state,"cities":city}
    return render(r,"data/view_donor.html",data)


def donorFilter(r,id=None):
    state=State.objects.all()
    city=City.objects.all()
    if id != None:
        data={"donors":Donor.objects.filter(d_state=id),"requestrs":Requester.objects.filter(r_state=id),
        "requestrscount":Requester.objects.filter(r_state=id).count(),
    "count":Donor.objects.filter(d_state=id).count(),
    "states":state,"cities":city}
        
    else:
        data={"donors":Donor.objects.filter(d_state=r.POST.get("d_state"),d_bloodGroup=r.POST.get("d_bloodGroup"),d_city=r.POST.get("d_city")),
    "count":Donor.objects.filter(d_state=r.POST.get("d_state"),d_bloodGroup=r.POST.get("d_bloodGroup"),d_city=r.POST.get("d_city")).count(),
    "states":state,"cities":city}
   
    return render(r,"data/view_donor.html",data)


def requestView(r):
    state=State.objects.all()
    city=City.objects.all()
    data={"requestrs":Requester.objects.all(),"count":Requester.objects.all().count(),"states":state,"cities":city}
    return render(r,"data/view_requester.html",data)


def requestFilter(r):
    state=State.objects.all()
    city=City.objects.all()
    data={"requestrs":Requester.objects.filter(r_state=r.POST.get("d_state"),r_bloodGroup=r.POST.get("d_bloodGroup"),r_city=r.POST.get("d_city")),
    "count":Requester.objects.filter(r_state=r.POST.get("d_state"),r_bloodGroup=r.POST.get("d_bloodGroup"),r_city=r.POST.get("d_city")).count(),
    "states":state,"cities":city}
    return render(r,"data/view_requester.html",data)


@csrf_exempt
def fetchCity(r):
    city=City.objects.filter(city_id = r.POST.get('d_state')).values()
    donors=Donor.objects.filter(d_state= r.POST.get('d_state')).values()
    #donor_city=Donor.objects.filter(d_city=r.POST.get('d_city')).values()
    donorcount=Donor.objects.filter(d_state= r.POST.get('d_state')).values().count()
    requester=Requester.objects.filter(r_state= r.POST.get('d_state')).values()
    requestercount=Requester.objects.filter(r_state= r.POST.get('d_state')).values().count()
    
    return JsonResponse({
        "cities":list(city),
        "donors":list(donors),
        "requesters":list(requester),
        "requestercount":requestercount,
        "donorcount":donorcount,
        
        },safe=False)