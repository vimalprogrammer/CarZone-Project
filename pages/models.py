from django.db import models

# Create your models here.

class Team(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')#pillow library installed
    facebook = models.URLField(max_length=100)
    twitter = models.URLField(max_length=100)
    google_plus = models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name #returns the first name of the team member in the admin page