"""django_alwar_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from . import views

urlpatterns = [
    path('home/',views.redirect_to_homepage,name='home'),
    path('data_admin/',views.redirect_to_admin,name='data_admin'),
    path('add_event/',views.redirect_to_event,name='add_event'),

    path('update_whattsapp/',views.redirect_to_update_whattapp,name='update_whattsapp'),
    path('update_telegram/',views.redirect_to_update_telegram,name='update_telegram'),

    path('add_people/',views.redirect_to_member,name='add_people'),
    path('display_member/',views.redirect_to_member_list,name='display_member'),

    path('add_feedback/',views.redirect_to_add_feedback,name='add_feedback'),
    path('display_data/',views.display_data,name='display_data'),
    path('remove_data/<int:id>',views.remove_data,name='remove_data'),
]
