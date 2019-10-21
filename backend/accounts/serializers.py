from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from .models import MyUser


class CustomRegisterSerializer(RegisterSerializer):

    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    nickname = serializers.CharField(required=True)

    # def validate_email(self, email):
    #     email = get_adapter().clean_email(email)
    #     if email and email_address_exists(email):
    #         raise serializers.ValidationError(
    #             _("A user is already registered with this e-mail address."))
    #     return email


    # def validate_password(self, password):
    #     return get_adapter().clean_password(password)


    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()

        return {
            'password': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'nickname': self.validated_data.get('nickname', ''),
        }


    def save(self, request):
        user = get_user_model()
        cleaned_data = self.get_cleaned_data()
        user.objects.create_user(**cleaned_data)
        return user
    

class CustomUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('email','nickname')
        read_only_fields = ('email',)