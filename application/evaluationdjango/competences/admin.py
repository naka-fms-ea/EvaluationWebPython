from django.contrib import admin

from .models import Skill, User

# Register your models here.

class SkillAdmin(admin.ModelAdmin):
    list_display = ('sk_name', 'sk_description')
    list_filter = ('sk_name', 'sk_description')
    ordering = ('sk_name', 'sk_description')
    search_fields = ['sk_name', 'sk_description']

class UserAdmin(admin.ModelAdmin):
    list_display = ('us_first_name', 'us_last_name', 'us_email', 'us_login', 'us_password')
    list_filter = ('us_first_name', 'us_last_name', 'us_email', 'us_login', 'us_password')
    ordering = ('us_first_name', 'us_last_name', 'us_email', 'us_login', 'us_password')
    search_fields = ['us_first_name', 'us_last_name', 'us_email', 'us_login', 'us_password']

admin.site.register(Skill, SkillAdmin)
admin.site.register(User, UserAdmin)