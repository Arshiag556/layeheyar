from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import random  # فرض بر این است که تابع ارسال کد تأیید در اینجا قرار دارد



def index(request):
    return render(request, "index.html")
