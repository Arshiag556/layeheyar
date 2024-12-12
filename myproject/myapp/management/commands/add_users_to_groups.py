from django.core.management.base import BaseCommand
from myapp.models import UserAccount  # از مدل سفارشی UserAccount استفاده کنید
from django.contrib.auth.models import Group  # وارد کردن مدل Group

class Command(BaseCommand):
    help = 'Adds users to specific groups'

    def add_user_to_group(self, identifier, group_name):
        """ تابع کمکی برای اضافه کردن کاربر به گروه """
        try:
            # جستجو برای کاربر با شماره تلفن وارد شده
            user = UserAccount.objects.filter(phone_number=identifier.strip()).first()

            if user is not None:  # اگر کاربر پیدا شد
                group, created = Group.objects.get_or_create(name=group_name)
                user.groups.add(group)
                self.stdout.write(
                    self.style.SUCCESS(f'User with phone_number {identifier} added to the {group_name} group'))
            else:  # اگر کاربر پیدا نشد
                self.stdout.write(self.style.ERROR(f'User with identifier {identifier} not found'))

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error adding user with identifier {identifier} to group {group_name}: {str(e)}'))
    def handle(self, *args, **kwargs):
        # اضافه کردن کاربران به گروه‌ها با استفاده از تابع کمکی
        self.add_user_to_group('09369516811', 'پشتیبانی فنی')  # به جای phone_number از فیلد مناسب خود استفاده کنید

