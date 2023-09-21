from rest_framework import serializers
from rest_framework import validators
# from django.contrib.auth.models import User
from .models import User_Profile

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User_Profile
        # fields=('first_name','last_name','username','email','password',)
        fields='__all__'
        
        extra_kwargs={
            "password":{"write_only": True},
            "email":{
                "required":True,
                "validators":[
                    validators.UniqueValidator(
                        User_Profile.objects.all(),"already exists !"
                    )
                ]
            }
        }
    def create(self,validated_data):
        first_name=validated_data.get('first_name')
        last_name=validated_data.get('last_name')
        username=validated_data.get('username')        
        email=validated_data.get('email')
        password=validated_data.get('password')
        
        user=User_Profile.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,            
            email=email,
            password=password,
        
        )
    
