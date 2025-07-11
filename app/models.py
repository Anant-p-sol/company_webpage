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


    def __str__(self):
        return self.company_name
    
class Service(models.Model):
    icon = models.CharField(max_length=50,blank=True, null=True) 
    tittle = models.CharField(max_length=150 , unique=True)
    description = models.TextField()


    def __str__(self):
        return self.tittle


class Testinomial(models.Model):
    user_image = models.CharField(max_length=255, blank=True, null=True)

    star_count = [
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
    ]
    rating_count = models.IntegerField(choices=star_count )
    user_name = models.CharField(max_length=100)
    user_job_title = models.CharField(max_length=100)
    review = models.TextField()

    def __str__(self):
        return f"{self.user_name} - {self.user_job_title}"
    
class FrequentlyAskedQuestion(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question

class Company(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    open_hours = models.CharField(max_length=100)

    video_url = models.URLField(blank=True, null=True)

    twitter_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
