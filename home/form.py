from .models import UserFeedback
from .models import TelegramGroup
from .models import WhattsappGroup
from .models import UserEvent
from .models import UserEventImage
from .models import Schedule
from .models import Speaker
from .models import Team
from .models import TeamPosition

from django import forms

class UserFeedBackForm(forms.ModelForm):
    class Meta:
        model = UserFeedback
        fields = [
            'name',
            'email',
            'contact',
            'query',
        ]

class WhattsappGroupForm(forms.ModelForm):
    class Meta:
        model = WhattsappGroup
        fields = [
            'group_name',
            'contact',
            'whattsapp_url',
        ]
        labels = {
            'whattsapp_url': 'Whattapp Link'
        }

class TelegramGroupForm(forms.ModelForm):
    class Meta:
        model = TelegramGroup
        fields = [
            'group_name',
            'contact',
            'telegram_url',
        ]
        labels = {
            'telegram_url': 'Telegram Link'
        }

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            'name',
            'user_image',
            'linkedin_url',
            'github_url',
            'about_member',
            'current_status',
            'college',
        ]
        labels = {
            'user_image':'Profile Picture',
            'linkedin_url': 'LinkedIn Link',
            'github_url': 'Github Link',
            'about_member': 'About',
            'current_status': 'Current Status',
        }

class TeamPositionForm(forms.ModelForm):
    class Meta:
        model = TeamPosition
        fields = [
            'position',
        ]

class UserEventForm(forms.ModelForm):
    class Meta:
        model = UserEvent
        fields =[
            'event_name',
            'cover_image',
            'address',
        ]

class UserEventImageForm(forms.ModelForm):
    class Meta:
        model = UserEventImage
        fields = [
            'album',
        ]

class SpeakerForm(forms.ModelForm):
    class Meta:
        model = Speaker
        fields = [
            'speaker_name',
            'speaker_image',
            'github_account',
            'linkedin_account',
            'about_speaker',
        ]

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = [
            'schedule_name',
            'start_time',
            'end_time',
            'description',
        ]