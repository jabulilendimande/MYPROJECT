from django.db import models

# Create your models here. This is the data I want to show on website from the database
class Test_app(models.Model):
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)