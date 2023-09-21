from django.db import models

# Create your models here.
class Profile(models.Model):
    first_name=models.CharField(max_length=50,default="")
    last_name=models.CharField(max_length=50,default="")
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name
    

