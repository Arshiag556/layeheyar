from django.db import models
from myapp.models import UserAccount
from jalali_date import date2jalali, datetime2jalali


class Document(models.Model):
    # عنوان لایحه
    title = models.CharField(max_length=255)

    # متن کامل لایحه
    text = models.TextField(null=True)
    SUBJECT_CHOICES = (
        ('Chois', 'انتحاب'),
        ('economic', 'اقتصادی'),
        ('social', 'اجتماعی'),
        ('Cultural', 'فرهنگی و آموزشی'),
        ('legal', 'حقوقی'),
        ('other', 'سایر'),
    )
    subject = models.CharField(max_length=10, choices=SUBJECT_CHOICES, default='Chois')
    # وضعیت لایحه: در حال بررسی، تایید شده، رد شده و غیره
    STATUS_CHOICES = (
        ('pending', 'در حال بررسی'),
        ('approved', 'تایید شده'),
        ('rejected', 'رد شده'),
    )

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    # کاربری که لایحه را نوشته است (ارتباط با مدل User)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    receipt_image = models.ImageField(upload_to='documents/receipt_image/')
    Letterattachment = models.FileField(upload_to='documents/Letterattachment/')

    # تاریخ ثبت لایحه
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_jalali_date(self):
        return date2jalali(self.created_at)

    class Meta:
        ordering = ['-created_at']  # نمایش لایحه‌ها به ترتیب تاریخ ثبت


class assembly(models.Model):
    # عنوان لایحه
    title = models.CharField(max_length=255)

    # متن کامل لایحه
    text = models.TextField(null=True)
    SUBJECT_CHOICES = (
        ('Chois', 'انتحاب'),
        ('economic', 'اقتصادی'),
        ('social', 'اجتماعی'),
        ('Cultural', 'فرهنگی و آموزشی'),
        ('legal', 'حقوقی'),
        ('other', 'سایر'),
    )
    subject = models.CharField(max_length=10, choices=SUBJECT_CHOICES, default='Chois')
    # وضعیت لایحه: در حال بررسی، تایید شده، رد شده و غیره
    STATUS_CHOICES = (
        ('pending', 'در حال بررسی'),
        ('approved', 'تایید شده'),
        ('rejected', 'رد شده'),
    )

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    # کاربری که لایحه را نوشته است (ارتباط با مدل User)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    receipt_image = models.ImageField(upload_to='documents/receipt_image/')
    Letterattachment = models.FileField(upload_to='documents/Letterattachment/')

    # تاریخ ثبت لایحه
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_jalali_date(self):
        return date2jalali(self.created_at)
