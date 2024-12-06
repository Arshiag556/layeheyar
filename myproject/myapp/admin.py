from django.contrib import admin
from .models import UserAccount, Notification
from django.forms import ModelForm


# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ("name", "family", "phone_number", "is_active", "is_staff", "is_verified", "registration_date")
    list_filter = ["is_staff", "is_active", "is_verified"]


admin.site.register(UserAccount, MemberAdmin)


class NotificationForm(ModelForm):
    class Meta:
        model = Notification
        fields = ['message', 'message_type', 'users', 'is_active']

    # فرم برای نمایش کاربران فقط در صورت انتخاب اعلان خصوصی
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.message_type == 'private':
            self.fields['users'].queryset = UserAccount.objects.all()  # نمایش همه کاربران برای اعلان خصوصی
        else:
            self.fields['users'].required = False  # برای اعلان عمومی نیازی به انتخاب کاربر نیست


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('message', 'created_at', 'message_type', 'is_active')
    list_filter = ('message_type', 'is_active')
    search_fields = ('message',)
    form = NotificationForm


admin.site.register(Notification, NotificationAdmin)



