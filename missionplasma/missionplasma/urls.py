"""missionplasma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from data.views import HomeView,insertDonor,fetchCity,insertRequester,donorView,requestView,donorFilter,requestFilter




urlpatterns = [
    path('admin/', admin.site.urls),
    path("",HomeView.as_view(),name="homepage"),
    path("donor/",insertDonor,name="donorform"),
    path("donorview/",donorView,name="donorview"),
    path("donorfilter/",donorFilter,name="donorfilter"),
    path("donorfilter/<int:id>/",donorFilter,name="statewise"),
    path("requestview/",requestView,name="requestview"),
    path("requestfilter/",requestFilter,name="requestfilter"),
    path("requester/",insertRequester,name="requesterform"),
    path("donor/fetch-cities/",fetchCity,name="fetch-cities"),
    path("requester/fetch-cities/",fetchCity,name="fetch-cities"),
    path("donorview/fetch-cities/",fetchCity,name="fetch-cities"),
    #path("donorview/fetch-user/",fetchCity,name="fetch-user"),
    path("requestview/fetch-cities/",fetchCity,name="fetch-cities"),
    path("donorfilter/fetch-cities/",fetchCity,name="fetch-cities"),
    path("requestfilter/fetch-cities/",fetchCity,name="fetch-cities"),
    path("donorfilter/<int:id>/fetch-cities/",fetchCity,name="fetch-cities"),
]
