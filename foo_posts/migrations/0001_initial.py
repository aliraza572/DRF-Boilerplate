# Generated by Django 3.2.10 on 2024-01-08 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_management', '0003_userprofile_geolocation'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_management.userprofile')),
                ('dislikes', models.ManyToManyField(blank=True, related_name='post_dislikes', to='user_management.UserProfile')),
                ('likes', models.ManyToManyField(blank=True, related_name='post_likes', to='user_management.UserProfile')),
            ],
        ),
    ]
