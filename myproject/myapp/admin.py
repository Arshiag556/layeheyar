from django.contrib import admin
from .models import UserAccount, Notification
from django.forms import ModelForm


class MemberAdmin(admin.ModelAdmin):
    # فیلدهایی که در پنل ادمین باید نمایش داده شوند
    list_display = (
        "phone_number", "name", "family", "birth_date", "national_code", "is_active", "is_staff", "is_verified",
        "registration_date", 'groups_display'
    )

    # اضافه کردن فیلتر برای وضعیت
    list_filter = ["is_staff", "is_active", "is_verified"]

    # متد برای نمایش گروه‌ها
    def groups_display(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])

    groups_display.short_description = 'Groups'

    # اضافه کردن فیلتر برای گروه‌ها و مجوزها
    filter_horizontal = ('groups', 'user_permissions')


    

    # فیلدهای که در فرم ادمین قابل جستجو هستند
    search_fields = ('phone_number', 'name', 'family')


# ثبت پنل ادمین برای UserAccount
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



