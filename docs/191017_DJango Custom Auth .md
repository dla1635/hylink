# Django Custom Auth



## Auth 설정을 위한 초기 환경 설정

### pip 설치 

```bash
$ pip install django-rest-auth django-allauth django-rest-framework django-cors-headers djangorestframework-jwt
```

```bash
#pip list를 했을 때 추가되는 것들
django-allauth         
django-cors-headers     
django-rest-auth        
django-rest-framework  
djangorestframework     
djangorestframework-jwt 
```



### settings/dev.py

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',  
    'django.contrib.staticfiles',
    
    # 로그인 기능을 위한 추가앱 
    'django.contrib.sites',
    'rest_auth',
    'rest_auth.registration',

    # SNS 로그인
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # RESTful API 
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',

    # 생성한 앱들 
    'backend.api',
    'backend.posts',
    'backend.links',
    'backend.accounts',
]
```

Middleware 설정 

```python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # 반드시 최상단
    ...
]
```

corheaders 설정

```python
CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = [
    "http://127.0.0.1:8080"
]

COR_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT'
)

CORS_ALLOW_HEADERS = (
'accept',
'accept-encoding',
'authorization',
'access-control-request-method',
'access-control-request-headers',
'content-type',
'dnt',
'origin',
'user-agent',
'x-csrftoken',
'x-requested-with',
)
```

Auth Model 설정 

>  Custum User Model을 아직 안만들었기 때문에 
>
> 일단 주석 처리 했습니다.

```python
import datetime

# AUTH_USER_MODEL = "app이름.앱에 있는 유저 모델 class 이름"
SITE_ID = 1
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework.authentication.TokenAuthentication',
    'rest_framework.authentication.SessionAuthentication',
    'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
    'rest_framework.permissions.IsAuthenticated',
    ),
}
#JWT_AUTH 설정을 위해 settings.py 맨 위해 import datetime을 추가하자!!
JWT_AUTH = {
    # If the secret is wrong, it will raise a jwt.DecodeError telling you as such. You can still get at the payload by setting the JWT_VERIFY to False.
    'JWT_VERIFY': True,
    # You can turn off expiration time verification by setting JWT_VERIFY_EXPIRATION to False.
    # If set to False, JWTs will last forever meaning a leaked token could be used by an attacker indefinitely.
    'JWT_VERIFY_EXPIRATION': True,
    # This is an instance of Python's datetime.timedelta. This will be added to datetime.utcnow() to set the expiration time.
    # Default is datetime.timedelta(seconds=300)(5 minutes).
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=1),
    'JWT_ALLOW_REFRESH': True,
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}
REST_USE_JWT = True

```



## Custom Auth Model 

### accounts/models.py

BaseUserManager와 AbstractBaseUser를 이용해 새로운 모델을 만들어줍니다.

```python
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

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password = password,
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
        Unique=True,
    )

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

```



### accounts/admin.py

관리자 페이지에서 Custom User Model을 활용할 수 있도록

입력창을 커스터마이징 해줍니다. 

```python
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import MyUser 

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'nickname')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'nickname', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'nickname', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('nickname',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nickname', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
```



### settings/dev.py

```python
AUTH_USER_MODEL = 'accounts.MyUser'
```



최종적으로 기존에 만들어둔 migrations 파일들을 모두 초기화해줍니다. 

다시 makemigrations 와 migrate을 진행한 뒤, admin 페이지를 실행하면

커스터마이징된 관리자 페이지를 확인할 수 있습니다. 



## 참고문헌

- [장고공식문서](https://docs.djangoproject.com/en/2.2/topics/auth/customizing/)