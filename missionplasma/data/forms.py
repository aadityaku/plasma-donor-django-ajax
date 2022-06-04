from tkinter.tix import Select
from django import forms
from .models import * 
GENDER_CHOICES=[
    ("ML","male"),
    ("FE","female"),
    ("OH","others"),
]
GROUP_CHOICES=[
    ("O+","O+"),
    ("A+","A+"),
    ("B+","B+"),
    ("AB+","AB+"),
    ("O-","O-"),
    ("A+","A-"),
    ("AB-","AB-"),
]

class DonorForm(forms.Form):
    d_name=forms.CharField(max_length=200,label="Name")
    d_gender=forms.CharField(widget=forms.RadioSelect(choices=GENDER_CHOICES),label="Gender")
    d_age=forms.IntegerField(min_value=18,label="Age")
    d_bloodGroup=forms.CharField(widget=forms.RadioSelect(choices=GROUP_CHOICES),label="Blood Group")
    d_covid_pos_date=forms.DateField(label="Covid positive date",widget=forms.TextInput(attrs={"type":"date"}))
    d_covid_neg_date=forms.DateField(label="Covid negative date",widget=forms.TextInput(attrs={"type":"date"}))
    #d_state=forms.ChoiceField(choices=[(x.id,x.state) for x in State.objects.all()],label="State")
    
    #d_city=forms.ChoiceField(choices=[(x.id,x.city_id,x.city) for x in City.objects.all()],label="City")
class RequesterForm(forms.Form):
    r_name=forms.CharField(max_length=200,label="Name")
    r_gender=forms.CharField(widget=forms.RadioSelect(choices=GENDER_CHOICES),label="Gender")
    r_age=forms.IntegerField(min_value=18,label="Age")
    r_bloodGroup=forms.CharField(widget=forms.RadioSelect(choices=GROUP_CHOICES),label="Blood Group")
    r_covid_pos_date=forms.DateField(label="Covid positive date",widget=forms.TextInput(attrs={"type":"date"}))
    r_covid_neg_date=forms.DateField(label="Covid negative date",widget=forms.TextInput(attrs={"type":"date"}))
    #d_state=forms.ChoiceField(choices=[(x.id,x.state) for x in State.objects.all()],label="State")
    
    #d_city=forms.ChoiceField(choices=[(x.id,x.city_id,x.city) for x in City.objects.all()],label="City")