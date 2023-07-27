from rest_framework import serializers
from account.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        password2=serializers.CharField(style={'input_type':'password'},write_only=True)
       
        fields=['email', 'name', 'password','password2','phone_number']
        model=User
        extra_kwargs={
            'password':{'write_only':True}

        }
    
    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        if password != password2 :
            raise serializers.ValidationError("Password didn't matched")
        return super().validate(attrs)
    
    def create(self,validate_data):
        return User.objects.create_user(**validate_data) 
    
class UserLoginSerializer(serializers.ModelSerializer):
    phone_number=serializers.CharField(max_length=11)
    class Meta:
        model=User
        fields=['phone_number', 'password']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','name','email','phone_number','photo']