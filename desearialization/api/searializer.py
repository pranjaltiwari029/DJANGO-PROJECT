from rest_framework import serializers
from .models import Student 

class StudentSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'rollNo', 'city']

        # it saves the data to the backend 
        def create(self, validated_data):
            return Student.objects.create(**validated_data)