from django.db import models
from django.contrib.auth.models import User

class Seeker_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    service = models.CharField(max_length=500)
    specialty = models.CharField(max_length=500)
    is_licensed = models.BooleanField()
    credentials = models.CharField(max_length=500)
    service_type = models.CharField(max_length=500)
    gender_identity = models.CharField(max_length=500)