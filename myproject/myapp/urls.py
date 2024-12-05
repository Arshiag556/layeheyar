from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include

import shora.views
from . import views
from .views import SignupView, verify_phone, user_login

urlpatterns = [

                  path('login/', user_login, name='login'),
                  path('singup/', SignupView.as_view(), name='singup'),

                  path('logout', views.logout_view.as_view(), name='logout'),
                  path("pannel/home/", views.home, name="home"),
                  path('verify-phone/<int:user_id>/', verify_phone, name='verify_phone'),
                  # آدرس برای ویو تأیید شماره تلفن
                  path('pannel/profile/', views.profile, name='profile'),
                  path('pannel/rules/', views.rules, name='rules'),
                  path('pannel/about/', views.about, name='about'),
                  path('pannel/contact-us/', views.contact_us, name='contact-us'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
