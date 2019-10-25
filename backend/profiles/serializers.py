from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# User Serializer
# 유저(사용자) 시리얼라이저는 간단하기도하고 Delete serializer와도 매우 유사합니다.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwards = {'password': {'write_only': True}}
 
    def create(self, validated_data):
        usere = User.objects.create_user(validated_data
        ['username'], validated_data['email'], validated_data['password'])
 
        return user


# Login Serializer
# 여기선 ModelSerializer로 선언하지 않습니다.
# 새롭게 만드는 것이 아닌 validate 즉, 로그인시 인증하는 용도이기 때문입니다.
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
 
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")