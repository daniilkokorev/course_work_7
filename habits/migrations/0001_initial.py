# Generated by Django 5.1 on 2024-08-07 16:13

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=120, verbose_name='Место выполнения привычки')),
                ('time', models.DateTimeField(verbose_name='Дата и время страта выполнения привычки')),
                ('action', models.CharField(max_length=235, verbose_name='Действие, которое требуется сделать')),
                ('pleasant_habit_sign', models.BooleanField(default=False, verbose_name='Признак приятной привычки')),
                ('periodicity', models.SmallIntegerField(default=1, help_text='Укажите периодичность от 1 до 7, где 1 - один раз в неделю, а 7 - это каждый день.', verbose_name='Периодичность выполнения привычки')),
                ('reward', models.CharField(blank=True, max_length=235, null=True, verbose_name='Награда за выполнение привычки')),
                ('duration', models.DurationField(default=datetime.timedelta(seconds=120), verbose_name='Продолжительность выполнения привычки')),
                ('is_published', models.BooleanField(default=True, verbose_name='Признак публичности')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='создатель привычки')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habits.habit', verbose_name='Связанная привычка')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
            },
        ),
    ]
