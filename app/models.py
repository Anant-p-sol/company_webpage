from django.db import models

# Create your models here.

class GeneralInfo(models.Model):
    company_name = models.CharField(max_length=300 ,default=" Company ")
    location = models.CharField(max_length=300)
    email = models.EmailField()
    phone = models.CharField(max_length=20)  # Increased max_length for international numbers
    open_hours = models.CharField(max_length=100, blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    