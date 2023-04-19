# Generated by Django 4.1.7 on 2023-04-19 18:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Seeker_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=500)),
                ('service', models.CharField(max_length=500)),
                ('specialty', models.CharField(max_length=500)),
                ('is_licensed', models.BooleanField()),
                ('credentials', models.CharField(max_length=500)),
                ('service_type', models.CharField(max_length=500)),
                ('gender_identity', models.CharField(max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]