from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

# 회원정보 관리는 Profile Model을 새롭게 작성할 예정 
# Cumstom User Model 은 username, email, password, nickname 입력 

class MyUserManager(BaseUserManager):
    def create_user(self, email, password, nickname):
        
        if not email:
            raise ValueError('이메일 주소를 입력해주세요')
        # TODO:passowrd, nickname도 에러메세지?
        user = self.model(
            email = self.normalize_email(email),
            nickname = nickname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, nickname):
        user = self.create_user(
            email,
            password = password,
            nickname = nickname
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    nickname = models.TextField(
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        "User가 특별한 허용 기능이 있습니까?"
        return True

    def has_module_perms(self, app_label):
        "User가 `app_label`을 볼 수 있는 권한이 있습니까?"
        return True

    @property
    def is_staff(self):
        "User가 스태프 멤버입니까?"
        return self.is_admin
