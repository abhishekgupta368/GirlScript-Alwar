from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.TelegramGroup)
admin.site.register(models.WhattsappGroup)

admin.site.register(models.UserFeedback)

admin.site.register(models.UserEvent)
admin.site.register(models.UserEventImage)
admin.site.register(models.Schedule)
admin.site.register(models.Speaker)

admin.site.register(models.Team)
admin.site.register(models.TeamPosition)