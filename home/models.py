from django.db import models

# Create your models here.
class TelegramGroup(models.Model):
    group_name = models.TextField(max_length=50,default='NULL')
    contact = models.TextField(max_length=20)
    telegram_url = models.TextField(max_length=100)

    def __str__(self):
        return self.contact
    
class WhattsappGroup(models.Model):
    group_name = models.TextField(max_length=50,default='NULL')
    contact = models.TextField(max_length=20)
    whattsapp_url = models.TextField(max_length=100)

    def __str__(self):
        return self.contact
    
class UserFeedback(models.Model):
    name = models.TextField(max_length=50)
    email = models.TextField(max_length=100)
    contact = models.TextField(max_length=20)
    query = models.TextField()

    def __str__(self):
        return self.name
    
class UserEvent(models.Model):
    event_name = models.TextField(max_length=100)
    cover_image = models.ImageField(upload_to='event_image',default='event_image/default.jpg')
    address = models.TextField(max_length=100)
    latitude = models.TextField(max_length=50)
    longitude = models.TextField(max_length=50)
    event_date = models.DateTimeField(auto_now=False)
    about_event = models.TextField()

    def __str__(self):
        return self.event_name

class UserEventImage(models.Model):
    event_name = models.ForeignKey(UserEvent,on_delete=models.CASCADE)
    album = models.ImageField(upload_to='album_image',default='album_image/default.jpg')

    def __str__(self):
        return self.event_name.event_name
    

class Schedule(models.Model):
    event_name = models.ForeignKey(UserEvent,on_delete=models.CASCADE)
    schedule_name = models.TextField(max_length=100)
    start_time = models.TimeField(auto_now=False)
    end_time = models.TimeField(auto_now=False)
    description = models.TextField()

    def __str__(self):
        return self.schedule_name
    
class Speaker(models.Model):
    event_name = models.ForeignKey(UserEvent,on_delete=models.CASCADE)
    speaker_name = models.TextField(max_length=50)
    speaker_image = models.ImageField(upload_to='speaker_image',default='speaker_image/default.jpg')
    github_account = models.TextField(max_length=100)
    linkedin_account = models.TextField(max_length=100)
    about_speaker = models.TextField(max_length=100)

    def __str__(self):
        return self.speaker_name


class Team(models.Model):
    name = models.TextField(max_length=100)
    user_image = models.ImageField(upload_to='profile_image',default='profile_image/default.jpg')
    linkedin_url = models.TextField(max_length=100)
    github_url = models.TextField(max_length=100)
    about_member = models.TextField()
    current_status = models.BooleanField()
    college = models.TextField(max_length=100)

    def __str__(self):
        return self.name

class TeamPosition(models.Model):
    name = models.ForeignKey(Team,on_delete=models.CASCADE)
    position = models.TextField(max_length=100)

    def __str__(self):
        return self.name.name+" -- " + self.position