from dataclasses import field
from phonenumbers import PhoneNumber
from rest_framework import serializers
from pharmacy.models import Medical

# For auth
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class MedicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medical
        fields = '__all__'
    

class RegisterSerializer(serializers.ModelSerializer):
    """
    To use this serializer, you must pass in the following data:
    {
        "username": "username",
        "email": "some-email@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "password": "password",
        "password2": "password"
    }

    To get the access token, you must perform a login with the credentials
    """
    email = serializers.EmailField(validators=[
                              UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validatePassword(self, attr):
        """
        This method is used to validate the password and password2 fields
        """
        if attr['password'] !=attr['password2']:
            raise serializers.ValidationError('Passwords must match')
        return attr


        
    def create(self, validated_data):
        """
        This method is used to create a new user
        """
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        # Set the user to staff
        user.is_staff = True
        user.set_password(validated_data['password'])
        user.save()

        return user