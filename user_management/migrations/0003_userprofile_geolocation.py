# Generated by Django 3.2.10 on 2024-01-08 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_auto_20240108_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='geolocation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
