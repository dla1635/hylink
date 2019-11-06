import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.utils import timezone

from django.db import models  
# from django.contrib.auth.models import User  
from django.db.models.signals import post_save  
from django.dispatch import receiver


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=is_staff, is_superuser=is_superuser, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,**extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=254, null=True, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(null=True)
    last_login = models.DateTimeField(null=True)
     
    USERNAME_FIELD = 'email'
    # EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        return self.username

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.username


    # @property
    # def token(self):
    #     """
    #     Allows us to get a user's token by calling `user.token` instead of
    #     `user.generate_jwt_token().

    #     The `@property` decorator above makes this possible. `token` is called
    #     a "dynamic property".
    #     """
    #     return self._generate_jwt_token()



    # def _generate_jwt_token(self):
    #     """
    #     Generates a JSON Web Token that stores this user's ID and has an expiry
    #     date set to 60 days into the future.
    #     """
    #     dt = datetime.now() + timedelta(days=60)

    #     token = jwt.encode({
    #         'id': self.pk,
    #         'exp': int(dt.strftime('%S'))
    #     }, settings.SECRET_KEY, algorithm='HS256')

    #     return token.decode('utf-8')

        

class Profile(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image_url = models.TextField(max_length=500, blank=True)
    withdraw = models.BooleanField(null=True, blank=True, default=False)
    withdraw_date = models.DateField(null=True, blank=True)


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):  
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):  
        instance.profile.save()