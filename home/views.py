from django.shortcuts import render,HttpResponse,redirect
from django.forms import formset_factory, modelformset_factory 

from .models import UserFeedback
from .models import WhattsappGroup
from .models import TelegramGroup
from .models import Team
from .models import TeamPosition
from .models import UserEvent,UserEventImage,Schedule,Speaker

from .form import UserFeedBackForm

from .form import UserEventForm,UserEventImageForm,ScheduleForm

from .form import WhattsappGroupForm,TelegramGroupForm
from .form import TeamForm,TeamPositionForm

from django import forms

# Create your views here.
def redirect_to_homepage(request):
    return render(request,'home.html')

#---------------------------------------------------------------------
def display_data(request):
    disp = UserFeedback.objects.all()
    user_data = {'user_data': disp}
    return render(request,'display_data.html',user_data)

def remove_data(request, id):
    try:
        instance = UserFeedback.objects.get(id=id)
        instance.delete()
        return redirect('display_feedback')
    except:
        return display_data(request)
#---------------------------------------------------------------------
def redirect_to_admin(request):
    return render(request,'administrator.html')

def redirect_to_member_list(request):
    all_members = Team.objects.all()
    all_position = TeamPosition.objects.all()
    context ={
        'model_data': all_members,
        'model_position': all_position
    }
    return render(request,'display_member.html',context)

def update_member_data(request,id):
    member_form = TeamForm(request.POST,request.FILES)
    if(request.method == 'POST'):
        member_info = Team.objects.get(pk= id)
        member_form = TeamForm(request.POST,request.FILES,instance=member_info)

        if member_form.is_valid():
            member_form.save()
            return redirect('display_member')
        
    else:
        member_info = Team.objects.get(pk= id)
        member_form = TeamForm(instance=member_info)
        print(member_info.linkedin_url)
        context ={
            'member_form':member_form
        }

        return render(request,'update_member_data.html',context)

def remove_member_data(request,id):
    instance = Team.objects.get(id=id)
    instance.delete()
    return redirect('display_member')
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
    event_data = UserEventForm(request.POST,request.FILES)
    if(event_data.is_valid()):
        event_data.save()
    context={
        'event_form':event_data
    }
    return render(request,'add_event.html',context)

def redirect_to_display_event(request):
    all_events = UserEvent.objects.all()
    all_speakers = Speaker.objects.all()
    all_images = UserEventImage.objects.all()
    all_schedule = Schedule.objects.all()

    context = {
        'member_information':all_events,
        'speaker_information': all_speakers,
        'image_information':all_images,
        'schedule_information':all_schedule
    }

    return render(request,'display_user_event.html',context)

def redirect_to_delete_event(request,id):
    instance = UserEvent.objects.get(pk=id)
    instance.delete()
    return redirect('display_user_event')
#------------------------------------------------------------
def manage_field_cnt(request):
    if(request.method == 'POST'):
        event_id =  request.POST['event_data_object']
        count = request.POST['member_cnt']
        print(event_id)
        print(count)
        return redirect('load_speaker_fields',event_id=event_id,cnt = count)

    else:
        instance = UserEvent.objects.all()
        context = {
            'dropdown_data_list':instance
        }
        return render(request,'manage_speaker.html',context)

def redirect_to_add_speaker(request,event_id,cnt):
    SpeakerForm = modelformset_factory(Speaker,fields =['speaker_name','speaker_image','github_account','linkedin_account','about_speaker'],extra = cnt) 
    formset = SpeakerForm(request.POST or None, request.FILES or None)
    UserEvent_instance = UserEvent.objects.get(pk = event_id)

    if formset.is_valid(): 
        for form in formset:
            speaker = Speaker(
                event_name = UserEvent_instance,
                speaker_name = form.cleaned_data.get('speaker_name'),
                speaker_image = form.cleaned_data.get('speaker_image'),
                github_account = form.cleaned_data.get('github_account'),
                linkedin_account = form.cleaned_data.get('linkedin_account'),
                about_speaker = form.cleaned_data.get('about_speaker'),
            )
            speaker.save()
    
    context = {
        'formset':formset
    }
    
    return render(request,'add_speaker.html',context)

def delete_speaker(request,id):
    instance = Speaker.objects.get(pk=id)
    instance.delete()
    return redirect('display_user_event')

def redirect_to_add_event_image(request):
    if(request.method == 'POST'):
        event_id =  request.POST['event_data_object']
        count = request.POST['image_cnt']
        return redirect('load_image_fields',event_id=event_id,cnt = count)

    else:
        instance = UserEvent.objects.all()
        context = {
            'dropdown_data_list':instance
        }
        return render(request,'manage_image.html',context)

def redirect_to_add_album(request,event_id,cnt):
    UserEventImageForm = modelformset_factory(UserEventImage,fields =['album'],extra = cnt) 
    formset = UserEventImageForm(request.POST or None, request.FILES or None)
    UserEvent_instance = UserEvent.objects.get(pk = event_id)

    if formset.is_valid(): 
        for form in formset:
            EventImage = UserEventImage(
                event_name = UserEvent_instance,
                album = form.cleaned_data.get('album'),
            )
            EventImage.save()
    
    context = {
        'formset':formset
    }
    
    return render(request,'add_image.html',context)

def redirect_delete_event_image(request,id):
    instance = UserEventImage.objects.get(pk=id)
    instance.delete()
    return redirect('display_user_event')
#-------------------------------------------------------------

def redirect_manage_schedule_cnt(request):
    if(request.method == 'POST'):
        event_id =  request.POST['event_data_object']
        count = request.POST['schedules_cnt']
        return redirect('load_schedule_fields',event_id=event_id,cnt = count)

    else:
        instance = UserEvent.objects.all()
        context = {
            'dropdown_data_list':instance
        }
        return render(request,'manage_schedule.html',context)

class DateInput(forms.DateInput):
    input_type = 'date'


def redirect_add_schedule_event(request,event_id,cnt):
    UserEventScheduleForm = modelformset_factory(Schedule,
                                                fields =['schedule_name','start_time','end_time','description'],
                                                widgets={
                                                    'start_time':DateInput(),
                                                    'end_time':DateInput(),
                                                },
                                                extra = cnt) 
    formset = UserEventScheduleForm(request.POST or None, request.FILES or None)
    UserEvent_instance = UserEvent.objects.get(pk = event_id)

    if formset.is_valid(): 
        for form in formset:
            EventSchedule = Schedule(
                event_name = UserEvent_instance,
                schedule_name = form.cleaned_data.get('schedule_name'),
                start_time = form.cleaned_data.get('start_time'),
                end_time = form.cleaned_data.get('end_time'),
                description = form.cleaned_data.get('description'),
            )
            EventSchedule.save()
    
    context = {
        'formset':formset
    }
    
    return render(request,'add_image.html',context)

def redirect_delete_schedule(request,id):
    Instance = Schedule.objects.get(pk = id)
    Instance.delete()
    return redirect('display_user_event')
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

#-----------------------------------------------------------------------------
# def redirect_to_add_schduel