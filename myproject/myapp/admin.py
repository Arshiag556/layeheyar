from django.contrib import admin
from .models import UserAccount


# Register your models here.

class MemberAdmin(admin.ModelAdmin):

    list_display = ( "name", "family", "phone_number", "is_active", "is_staff","is_verified", "registration_date")
    list_filter = ["is_staff", "is_active","is_verified"]



admin.site.register(UserAccount, MemberAdmin )




