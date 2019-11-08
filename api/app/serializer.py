from rest_framework import serializers
from django import forms
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' # Can use some fields only ('fieldName', 'fieldName')
        
        