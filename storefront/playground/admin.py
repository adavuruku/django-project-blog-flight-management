from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from django.forms import CharField, Textarea, TextInput
from django import forms
from playground.models import NewUser
# Register your models here.

class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields =('email', 'user_name','first_name',)
    list_filter =('email','first_name','is_active',)
    ordering =('-start_date',)
    list_display =('email', 'user_name','first_name','is_active', 'is_staff',)

    fieldsets = (
        (None, {'fields':('email', 'user_name', 'first_name',)}),
        ('Permissions', {'fields':('is_active', 'is_staff',)}),
        ('Personal', {'fields':('about',)}),
    )

    formfield_overrides = {
        # NewUser.TextField: {
        #     'widget':Textarea(attrs={
        #         'rows':20,
        #         'cols':60
        #     })
        # }
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')
        })
    )

# @admin.register(models.Post)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('title', 'id', 'status', 'slug', 'author')
#     populated_fields = {'slug': ('title',), }

admin.site.register(NewUser, UserAdminConfig)