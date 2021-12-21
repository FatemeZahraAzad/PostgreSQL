from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

from .forms import *

CustomUser = CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserCreationForm
    model = CustomUser
    list_display = ['email','username','is_staff', 'date_joined','is_active']
    list_display_link =['email','date_joined']
    list_editable = ['is_staff']
    empty_value_display = 'NULL'
    list_filter = ['email','is_active']
    list_per_page = 5
    search_field = ('username' , 'email')



admin.site.register(CustomUser , CustomUserAdmin)
