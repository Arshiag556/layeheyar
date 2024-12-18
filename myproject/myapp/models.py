from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone
from django.contrib.auth.models import Group,Permission
from jalali_date import date2jalali



class UserManager(BaseUserManager):
    def create_user(self, phone_number, name, family, birth_date, national_code, password=None):
        if not phone_number:
            raise ValueError('Users must have a phone number')

        user = self.model(
            phone_number=phone_number,
            name=name,
            family=family,
            birth_date=birth_date,
            national_code=national_code,
        )

        user.set_password(password)  # تنظیم رمز عبور با استفاده از متد set_password
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, name, family, birth_date, national_code, password=None):
        user = self.create_user(
            phone_number=phone_number,
            name=name,
            family=family,
            birth_date=birth_date,
            national_code=national_code,
            password=password
        )
        user.is_active = True
        user.is_verified = "4"  # وضعیت وریفای شده
        user.is_phone_verified = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class UserAccount(AbstractBaseUser):
    phone_number = models.CharField(max_length=15, default='0000000000', unique=True, verbose_name="شماره تلفن")
    card_number = models.CharField(max_length=16, null=True, blank=True)  # شماره کارت کاربر
    balance = models.DecimalField(max_digits=10, decimal_places=0, default=0)  # موجودی حساب
    name = models.CharField(max_length=100, verbose_name="نام")
    family = models.CharField(max_length=100, verbose_name="نام خانوادگی")
    state = models.CharField(max_length=150, blank=True, null=True, verbose_name="استان")
    city = models.CharField(max_length=150, blank=True, null=True, verbose_name="شهر")
    address = models.CharField(max_length=150, blank=True, null=True, verbose_name="آدرس")
    birth_date = models.DateField(blank=True, null=True, verbose_name="تاریخ تولد")
    id_card = models.ImageField(upload_to='id_cards/', blank=True, null=True, verbose_name="کارت ملی")
    national_code = models.CharField(max_length=100, blank=True, null=True, verbose_name="کدملی")
    selfie = models.ImageField(upload_to='selfie/', blank=True, null=True, verbose_name="عکس سلفی")
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True, verbose_name="عکس پروفایل")
    registration_date = models.DateTimeField(default=timezone.now, verbose_name="سال ساخت اکانت")
    verification_code = models.CharField(max_length=6, blank=True, null=True, verbose_name="کد وریفای")
    is_phone_verified = models.BooleanField(default=False, verbose_name="تایید شماره تلفن")
    is_active = models.BooleanField(default=False, verbose_name="فعال سازی حساب")
    STATUS = [
        ("1", "وریفای نشده"),
        ("2", "درحال بررسی"),
        ("3", "نیاز به تغییرات"),
        ("4", "وریفای شده"),
    ]
    is_verified = models.CharField(choices=STATUS, default="1", max_length=30, verbose_name="وضعیت وریفای حساب")
    is_staff = models.BooleanField(default=False, verbose_name="ادمین")
    groups = models.ManyToManyField(Group, blank=True)
    user_permissions = models.ManyToManyField(Permission, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'  # شماره تلفن به عنوان نام کاربری
    REQUIRED_FIELDS = ['name', 'family', 'birth_date', 'national_code']

    def __str__(self):
        return f"{self.phone_number} {self.name} {self.family} {self.registration_date}"

    def get_jalali_date(self):
        return date2jalali(self.birth_date)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_sha256$'):
            self.set_password(self.password)  # هش کردن رمز عبور
        super(UserAccount, self).save(*args, **kwargs)
    class Meta:
        verbose_name = "کاربر ها"
        verbose_name_plural = "کاربر ها"
class Notification(models.Model):
    MESSAGE_TYPES = (
        ('public', 'Public'),  # اعلان عمومی
        ('private', 'Private'),  # اعلان خصوصی
    )

    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_read = models.BooleanField(default=False)  # فیلد برای نشان دادن وضعیت خوانده‌شده
    message_type = models.CharField(max_length=10, choices=MESSAGE_TYPES, default='public')
    users = models.ManyToManyField(UserAccount, related_name='notifications', blank=True)  # کاربران خاص که اعلان رو می‌بینند

    def __str__(self):
        # اگر می‌خواهید پیامی که شامل شماره تلفن اولین کاربر است را نمایش دهید
        # این کد به طور فرضی اولین کاربر را می‌گیرد
        if self.users.exists():
            user = self.users.first()
            return f"Notification for {user.phone_number} - {self.message[:20]}"
        return self.message[:20]

class Payment(models.Model):
    account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    card_number=models.CharField(max_length=15, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    receipt_image = models.ImageField(upload_to='receipts/')
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment by {self.account.phone_number} - {self.amount} - Approved: {self.is_approved}"