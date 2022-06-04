from django.db import models
# Create your models here.


class State(models.Model):
    state=models.CharField(max_length=255, null=False, blank=False)
    def __str__(self):
        return self.state
class City(models.Model):
    city_id=models.ForeignKey(State,on_delete=models.CASCADE)
    city=models.CharField(max_length=200)

    def __str__(self):
        return self.city

class Donor(models.Model):
    d_name=models.CharField(max_length=200,blank=False,null=False)
    d_gender=models.CharField(max_length=200,blank=False,null=False)
    d_age=models.IntegerField()
    d_bloodGroup=models.CharField(max_length=200,blank=False,null=False)
    d_covid_pos_date=models.DateField()
    d_covid_neg_date=models.DateField()
    d_state=models.ForeignKey(State,on_delete=models.SET_NULL,null=True)
    d_city=models.ForeignKey(City,on_delete=models.CASCADE,null=True)
    

    def __str__(self):
        return self.d_name

class Requester(models.Model):
    r_name=models.CharField(max_length=200,blank=False,null=False)
    r_gender=models.CharField(max_length=200,blank=False,null=False)
    r_age=models.IntegerField()
    r_bloodGroup=models.CharField(max_length=200,blank=False,null=False)
    r_covid_pos_date=models.DateField()
    r_covid_neg_date=models.DateField()
    r_state=models.ForeignKey(State,on_delete=models.CASCADE,blank=False,null=False)
    r_city=models.ForeignKey(City,on_delete=models.CASCADE,blank=False,null=False)

    def __str__(self):
        return self.r_name

    