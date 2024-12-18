from django.contrib import admin
from .models import Document, assembly  # استفاده از نام‌های صحیح مدل‌ها

# ثبت مدل Document با تنظیمات ادمین
class ShoraAdmin(admin.ModelAdmin):  # استفاده از نام صحیح کلاس ادمین
    list_display = ('user',)  # اطمینان حاصل کنید که 'user' یک فیلد معتبر است

admin.site.register(Document, ShoraAdmin)

# ثبت مدل Assembly با تنظیمات ادمین
class AssemblyAdmin(admin.ModelAdmin):  # استفاده از نام صحیح کلاس ادمین
    list_display = ('user',)  # اطمینان حاصل کنید که 'user' یک فیلد معتبر است

admin.site.register(assembly, AssemblyAdmin)
