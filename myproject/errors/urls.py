from django.conf.urls import handler404, handler500
from errors.views import custom_404, custom_500  # ویوهای 404 و 500 سفارشی

handler404 = 'errors.views.custom_404'  # نام ویو برای صفحه 404
handler500 = 'errors.views.custom_500'  # نام ویو برای صفحه 500
