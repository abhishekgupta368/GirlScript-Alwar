from django.shortcuts import render,HttpResponse,redirect
from .models import UserFeedback
from .models import WhattsappGroup
from .models import TelegramGroup
from .models import Team
from .models import TeamPosition

from .form import UserFeedBackForm
from .form import WhattsappGroupForm,TelegramGroupForm
from .form import TeamForm,TeamPositionForm

# Create your views here.
def redirect_to_homepage(request):
    return render(request,'index.html')

#---------------------------------------------------------------------
def display_data(request):
    disp = UserFeedback.objects.all()
    user_data = {'user_data': disp}
    return render(request,'display_data.html',user_data)

def remove_data(request, id):
    # try:
        instance = UserFeedback.objects.get(id=id)
        instance.delete()
        return redirect('display_data')
    # except:
    #     return display_data(request)
#---------------------------------------------------------------------
def redirect_to_admin(request):
    return render(request,'administrator.html')

def redirect_to_member_list(request):
    all_members = Team.objects.all()
    all_position = TeamPosition.objects.all()
    print(all_position[0].name)
    context ={
        'model_data': all_members,
        'model_position': all_position
    }
    return render(request,'display_member.html',context)

#-----------------------------------------------------------------
def redirect_to_member(request):
    Team_data = TeamForm(request.POST, request.FILES)
    Team_position = TeamPositionForm(request.POST)

    if(Team_data.is_valid() and Team_position.is_valid()):
        print(Team_data.cleaned_data.get('user_image'))
        save_team = Team_data.save()
        save_team_positon = Team_position.save(commit=False)

        save_team_positon.name = save_team
        save_team_positon.save()
    
    # print(Team_data)

    context={
        'form1':Team_data,
        'form2':Team_position
    }

    return render(request,'add_member.html',context)

#-------------------------------------------------------------
def redirect_to_event(request):
    return render(request,'add_event.html')

#-------------------------------------------------------------
def redirect_to_update_whattapp(request):
    Whattsapp = WhattsappGroupForm(request.POST)
    if(Whattsapp.is_valid()):
        group_name = Whattsapp.cleaned_data.get("group_name")
        contact = Whattsapp.cleaned_data.get("contact")
        whattsapp_url = Whattsapp.cleaned_data.get("whattsapp_url")
        try:
            Whattapp_old_data = WhattsappGroup.objects.all()
            Whattapp_old_data.delete()

            Wgrp = WhattsappGroup(group_name = group_name, contact = contact,whattsapp_url = whattsapp_url)
            Wgrp.save()

        except:
            Wgrp = WhattsappGroup(group_name = group_name, contact = contact,whattsapp_url = whattsapp_url)
            Wgrp.save()

        # Whattsapp.data["group_name"] = ""
        # Whattsapp.data["contact"] = ""
        # Whattsapp.data["whattsapp_url"] = ""

    model = WhattsappGroup.objects.all()
    context ={
        'form':Whattsapp,
        'model':model
    }
    return render(request,'update_whattsapp.html',context)

def redirect_to_update_telegram(request):
    Telegram = TelegramGroupForm(request.POST)
    if(Telegram.is_valid()):
        group_name = Telegram.cleaned_data.get("group_name")
        contact = Telegram.cleaned_data.get("contact")
        telegram_url = Telegram.cleaned_data.get("telegram_url")
        try:
            Telegram_old_data = TelegramGroup.objects.all()
            Telegram_old_data.delete()

            Tgrp = TelegramGroup(group_name = group_name, contact = contact,telegram_url = telegram_url)
            Tgrp.save()
        except:
            Tgrp = TelegramGroup(group_name = group_name, contact = contact,telegram_url = telegram_url)
            Tgrp.save()

    model = TelegramGroup.objects.all()
    context ={
        'form':Telegram,
        'model':model
    }
    return render(request,'update_telegram.html',context)

#------------------------------------------------------------------------------
def redirect_to_add_feedback(request):
    UserForm = UserFeedBackForm(request.POST or None)
    if(UserForm.is_valid()):
        UserForm.save()

    context = {
            'form':UserForm
        }
    return render(request,'add_feedback.html',context)
