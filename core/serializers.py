from rest_framework import serializers
from .models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id','first_name','last_name','username'
        )

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators = [UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True
    )
    class Meta:
        model=User
        fields = (
            'username',
            'password',
            'password2',
            'email',
            'first_name',
            'last_name'
        )
        extra_kwargs = {
            'first_name': {
                'required': True
            },
            'last_name':{
                'required':True
            }
        }
    
    def validate(self,attrs):
        '''
        This function validates the password and password2 of the user.

        Args: attrs dictionary.
        Returns: attrs dictionary if validated. Else, raises error. 
        '''
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {
                    'password': 'Passwords do not match.'
                }
            )
        return attrs 

    def create(self,validated_data):
        '''
        This function creates user instance of the user if the query is validated.

        Args: validated_data dictionary.
        Returns: User object. 
        '''
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    
