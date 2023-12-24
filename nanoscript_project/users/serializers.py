from rest_framework import serializers
from .models import User
from rest_framework.serializers import Serializer, ModelSerializer, CharField
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User 
        fields = ('pk', 'name', 'email', 'description', 'registrationDate')
    
class IssueTokenRequestSerializer(Serializer):
    model = User
    
    username = CharField(required=True)
    password = CharField(required=True)
                         
class TokenSeriazliser(ModelSerializer):
    
    class Meta: 
        model = Token 
        fields = ['key']