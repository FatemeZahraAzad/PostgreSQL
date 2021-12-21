from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .models import *
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

class ChangeAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return Change.objects.exclude(status='closed')

class ClosedChangeAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return ClosedChange.objects.filter(status='closed')

class Line(admin.TabularInline):
    model = Change

inline = [Line]

admin.site.register(Change, ChangeAdmin)
admin.site.register(ClosedChange, ClosedChangeAdmin)

admin.site.register(CustomUser , CustomUserAdmin)
