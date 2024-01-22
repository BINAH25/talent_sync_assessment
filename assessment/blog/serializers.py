from .models import *
from rest_framework import serializers

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'last_name',
            'first_name',
            'id'
        ]
        
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        # CLEAN ALL VALUES
        username = validated_data['username'].lower()
        password = validated_data['password']
        # CREATE A NEW  USER
        user = User.objects.create(
            username=username,
        )
        user.set_password(password)
        user.save()
        return user
    
    
    
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'