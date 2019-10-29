from django.contrib import admin  
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin  
# from django.contrib.auth.models import User  
from django.contrib.auth import get_user_model

from .models import Profile


class ProfileInline(admin.StackedInline):  
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

    fields = ('image_url', 'withdraw', 'withdraw_date')


class UserAdmin(admin.ModelAdmin):  
    inlines = (ProfileInline, )


# admin.site.unregister(User)  
admin.site.register(get_user_model(), UserAdmin)
# admin.site.register(User, UserAdmin)
