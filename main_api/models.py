from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

class Provider_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    service = models.CharField(max_length=500)
    specialty = models.CharField(max_length=500)
    is_licensed = models.BooleanField()
    credentials = models.CharField(max_length=500)
    service_type = models.CharField(max_length=500)
    gender_identity = models.CharField(max_length=500)

# class Seeker_Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_photo = models.CharField(max_length=500)
#     location = models.CharField(max_length=500)
#     service = models.CharField(max_length=500)
#     interests = ArrayField(models.CharField(max_length=500), size=5)
#     goal = models.CharField(max_length=500)
#     similar_interest = models.BooleanField()
#     service_preference = models.CharField(max_length=500)
#     gender_preference = models.CharField(max_length=500)