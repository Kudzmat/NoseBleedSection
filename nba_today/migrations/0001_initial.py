# Generated by Django 4.2.4 on 2023-12-18 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_id', models.CharField(max_length=50, unique=True)),
                ('team_name', models.CharField(max_length=50)),
                ('logo_url', models.URLField()),
            ],
        ),
    ]
