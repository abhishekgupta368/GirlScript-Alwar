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
    path('display_user_event/',views.redirect_to_display_event,name='display_user_event'),
    path('delete_user_member/<int:id>',views.redirect_to_delete_event,name='delete_user_member'),

    path('add_speaker/',views.manage_field_cnt,name='add_speaker'),
    path('delete_speaker/<int:id>',views.delete_speaker,name='delete_speaker'),
    path('load_speaker_fields/<int:event_id>/<int:cnt>/',views.redirect_to_add_speaker,name='load_speaker_fields'),

    path('add_schedule/',views.redirect_manage_schedule_cnt,name='add_schedule'),
    path('delete_schedule/<int:id>',views.redirect_delete_schedule,name='delete_schedule'),
    path('load_schedule_fields/<int:event_id>/<int:cnt>/',views.redirect_add_schedule_event,name='load_schedule_fields'),

    path('add_event_image/',views.redirect_to_add_event_image,name='add_event_image'),
    path('delete_event_image/<int:id>',views.redirect_delete_event_image,name='delete_event_image'),
    path('load_image_fields/<int:event_id>/<int:cnt>/',views.redirect_to_add_album,name="load_image_fields"),

    path('update_whattsapp/',views.redirect_to_update_whattapp,name='update_whattsapp'),
    path('update_telegram/',views.redirect_to_update_telegram,name='update_telegram'),

    path('add_member/',views.redirect_to_member,name='add_member'),
    path('display_member/',views.redirect_to_member_list,name='display_member'),
    path('update_member_data/<int:id>',views.update_member_data,name='update_member_data'),
    path('remove_member_data/<int:id>',views.remove_member_data,name='remove_member_data'),

    path('add_feedback/',views.redirect_to_add_feedback,name='add_feedback'),
    path('display_feedback/',views.display_data,name='display_feedback'),
    path('remove_feedback/<int:id>',views.remove_data,name='remove_feedback'),
]
