from django.db import models

# Create your models here.
class TelegramGroup(models.Model):
    group_name = models.CharField(max_length=50,default='NULL', blank=False)
    contact = models.CharField(max_length=20, blank=False)
    telegram_url = models.URLField(max_length=200, blank=False)

    def __str__(self):
        return self.contact
    
class WhattsappGroup(models.Model):
    group_name = models.CharField(max_length=50,default='NULL', blank=False)
    contact = models.CharField(max_length=20, blank=False)
    whattsapp_url = models.URLField(max_length=200, blank=False)

    def __str__(self):
        return self.contact
    
class UserFeedback(models.Model):

    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=200, blank=False)
    contact = models.CharField(max_length=20, blank=False)
    query = models.TextField(blank=False)

    def __str__(self):
        return self.name
    
class UserEvent(models.Model):
    event_name = models.CharField(max_length=100,blank=False)
    cover_image = models.ImageField(upload_to='event_image', blank=False)
    address = models.CharField(max_length=100,blank=False)
    latitude = models.CharField(max_length=50,blank=False)
    longitude = models.CharField(max_length=50,blank=False)
    event_date = models.DateTimeField(auto_now=False, blank=False)
    about_event = models.TextField(blank=False)

    def __str__(self):
        return self.event_name

class UserEventImage(models.Model):
    event_name = models.ForeignKey(UserEvent,on_delete=models.CASCADE)
    album = models.ImageField(upload_to='album_image', blank=False)

    def __str__(self):
        return self.event_name.event_name
    

class Schedule(models.Model):
    event_name = models.ForeignKey(UserEvent,on_delete=models.CASCADE)
    schedule_name = models.CharField(max_length=100,blank=False)
    start_time = models.DateTimeField(auto_now=False, blank=False)
    end_time = models.DateTimeField(auto_now=False, blank=False)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.schedule_name
    
class Speaker(models.Model):
    event_name = models.ForeignKey(UserEvent,on_delete=models.CASCADE)
    speaker_name = models.CharField(max_length=50,blank=False)
    speaker_image = models.ImageField(upload_to='speaker_image', blank=False)
    github_account = models.URLField(max_length=100, blank=False)
    linkedin_account = models.URLField(max_length=100, blank=False)
    about_speaker = models.TextField(max_length=100,blank=False)

    def __str__(self):
        return self.speaker_name


class Team(models.Model):
    name = models.CharField(max_length=100,blank=False)
    user_image = models.ImageField(upload_to='profile_image', blank=False)
    linkedin_url = models.URLField(max_length=100, blank=False)
    github_url = models.URLField(max_length=100, blank=False)
    about_member = models.TextField(blank=False)
    STATUS = [('0','NO'),('1','YES')]
    current_status = models.CharField(max_length=4,choices=STATUS,default='1',blank=False)
    college = models.CharField(max_length=100,blank=False)

    def __str__(self):
        return self.name

class TeamPosition(models.Model):
    name = models.ForeignKey(Team,on_delete=models.CASCADE)
    position = models.CharField(max_length=100,blank=False)

    def __str__(self):
        return self.name.name+" -- " + self.position