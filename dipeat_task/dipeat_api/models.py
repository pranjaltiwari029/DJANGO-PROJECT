from django.db import models

# Create your models here
class User_Profile(models.Model):
    first_name=models.CharField(max_length=50,blank=False)
    last_name=models.CharField(max_length=50,blank=False)
    username=models.CharField(max_length=50,blank=False)
    email=models.EmailField(max_length=50, unique=True,blank=False)
    # Phone_no=models.IntegerField()
    
    password=models.CharField(max_length=20,blank=False)
    
