from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from myapp.models import UserAccount # مدل‌هایی که می‌خواهیم به آن‌ها دسترسی بدهیم
from tickets.models import Ticket
# 1. ایجاد گروه‌ها
technical_support_group, created = Group.objects.get_or_create(name='پشتیبانی فنی')
user_admin_group, created = Group.objects.get_or_create(name='مدیر کاربران')
support_group, created = Group.objects.get_or_create(name='پشتیبانی')

# 2. دسترسی‌های مربوط به پشتیبانی فنی
technical_support_permissions = [
    ('view_user', UserAccount),   # مشاهده کاربران
    ('change_user', UserAccount), # ویرایش کاربران
    ('delete_user', UserAccount), # حذف کاربران
]

# 3. دسترسی‌های مربوط به مدیر کاربران
user_admin_permissions = [
    ('view_user', UserAccount),   # مشاهده کاربران
    ('change_user', UserAccount), # ویرایش کاربران
    ('add_user', UserAccount),    # اضافه کردن کاربران
]

# 4. دسترسی‌های مربوط به پشتیبانی
support_permissions = [
    ('view_ticket', Ticket),     # مشاهده تیکت‌ها
    ('change_ticket', Ticket),   # ویرایش تیکت‌ها
    ('close_ticket', Ticket),    # بستن تیکت‌ها
]

# اضافه کردن دسترسی‌ها به گروه‌ها
def add_permissions_to_group(group, permissions):
    for perm_codename, model in permissions:
        content_type = ContentType.objects.get_for_model(model)
        try:
            permission = Permission.objects.get(codename=perm_codename, content_type=content_type)
            group.permissions.add(permission)
        except Permission.DoesNotExist:
            print(f"Permission '{perm_codename}' not found for model '{model.__name__}'")

# اضافه کردن مجوزها به گروه‌های مختلف
add_permissions_to_group(technical_support_group, technical_support_permissions)
add_permissions_to_group(user_admin_group, user_admin_permissions)
add_permissions_to_group(support_group, support_permissions)
