# Generated by Django 4.2.4 on 2024-10-01 19:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nba_stats', '0003_leagueleaders'),
    ]

    operations = [
        migrations.AddField(
            model_name='careerawards',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]
