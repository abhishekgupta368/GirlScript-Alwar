# Generated by Django 3.0.7 on 2020-06-09 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user_image', models.ImageField(upload_to='profile_image')),
                ('linkedin_url', models.URLField(max_length=100)),
                ('github_url', models.URLField(max_length=100)),
                ('about_member', models.TextField()),
                ('current_status', models.CharField(choices=[('0', 'NO'), ('1', 'YES')], default='1', max_length=4)),
                ('college', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TelegramGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(default='NULL', max_length=50)),
                ('contact', models.CharField(max_length=20)),
                ('telegram_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='UserEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('cover_image', models.ImageField(upload_to='event_image')),
                ('address', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=50)),
                ('longitude', models.CharField(max_length=50)),
                ('event_date', models.DateTimeField()),
                ('about_event', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=200)),
                ('contact', models.CharField(max_length=20)),
                ('query', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WhattsappGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(default='NULL', max_length=50)),
                ('contact', models.CharField(max_length=20)),
                ('whattsapp_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='UserEventImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.ImageField(upload_to='album_image')),
                ('event_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.UserEvent')),
            ],
        ),
        migrations.CreateModel(
            name='TeamPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speaker_name', models.CharField(max_length=50)),
                ('speaker_image', models.ImageField(upload_to='speaker_image')),
                ('github_account', models.URLField(max_length=100)),
                ('linkedin_account', models.URLField(max_length=100)),
                ('about_speaker', models.TextField(max_length=100)),
                ('event_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.UserEvent')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_name', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('description', models.TextField()),
                ('event_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.UserEvent')),
            ],
        ),
    ]
