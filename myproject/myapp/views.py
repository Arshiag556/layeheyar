from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .forms import SignupForm, LoginForm, CompleteProfileForm, PhoneVerificationForm
from .models import UserAccount,Notification
from django.contrib.auth.decorators import login_required
import random
from .utils import send_verification_code  # فرض بر این است که تابع ارسال کد تأیید در اینجا قرار دارد
from django.contrib.auth import update_session_auth_hash
from tickets.models import Ticket
from shora.models import assembly,Document
from django.db.models import Q



class SignupView(View):
    form_class = SignupForm
    initial = {}
    template_name = "loginorsingup/singup.html"

    def dispatch(self, request, *args, **kwargs):
        # اگر کاربر لاگین باشد، او را به صفحه پنل کاربری هدایت کن
        if request.user.is_authenticated:
            return redirect('home')  # 'user_panel' را با مسیر دلخواه جایگزین کنید
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.is_active = False
            user.save()

            # ذخیره شماره تلفن و ایجاد کد تأیید
            phone_number = form.cleaned_data.get('phone_number')
            verification_code = str(random.randint(100000, 999999))  # کد تأیید ۶ رقمی تصادفی

            user.phone_number = phone_number
            user.verification_code = verification_code
            user.save()

            # ارسال کد تأیید به شماره تلفن
            send_verification_code(phone_number, verification_code)

            messages.success(request, 'لطفاً شماره تلفن خود را تأیید کنید.')
            return redirect('verify_phone', user_id=user.id)  # هدایت کاربر به صفحه تأیید شماره تلفن

        return render(request, self.template_name, {'form': form})



def verify_phone(request, user_id):
    user = get_object_or_404(UserAccount, pk=user_id)

    if request.method == 'POST':
        form = PhoneVerificationForm(request.POST)
        if form.is_valid():
            verification_code = form.cleaned_data['verification_code']
            if user.verification_code == verification_code:
                user.is_phone_verified = True
                user.verification_code = None  # حذف کد تأیید بعد از تأیید
                user.save()

                # بعد از تایید شماره تلفن، حساب کاربری فعال می‌شود
                user.is_active = True
                user.save()

                messages.success(request, 'شماره تلفن شما با موفقیت تأیید شد.')
                return redirect('login')
            else:
                messages.error(request, 'کد تأیید اشتباه است. لطفاً دوباره تلاش کنید.')
    else:
        form = PhoneVerificationForm()

    return render(request, 'loginorsingup/verify_phone.html', {'form': form})


from django.shortcuts import redirect

def user_login(request):
    # اگر کاربر لاگین شده باشد، او را به صفحه پنل هدایت کن
    if request.user.is_authenticated:
        return redirect('home')  # 'user_panel' را با مسیر دلخواه جایگزین کنید

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']

            try:
                user = UserAccount.objects.get(phone_number=phone_number)
            except UserAccount.DoesNotExist:
                user = None

            if user is not None and user.check_password(password):
                if user.is_phone_verified and user.is_active:
                    auth_login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, 'حساب کاربری شما فعال نشده است یا شماره تلفن تأیید نشده است.')
            else:
                messages.error(request, 'شماره تلفن یا رمز عبور اشتباه است.')

    else:
        form = LoginForm()

    return render(request, 'loginorsingup/login.html', {'form': form})



class logout_view(View):
    def get(self, request):
        request.session.clear()
        return redirect('login')


@login_required
def profile(request):
    if request.method == 'POST':
        form = CompleteProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            if request.user.is_verified == "1" or request.user.is_verified == "3":
                request.user.is_verified = "2"
            else:
                request.user.is_verified = "4"

            # چک کردن تغییر پسورد
            password = form.cleaned_data.get('password')
            if password:
                request.user.set_password(password)  # به روز رسانی پسورد

            form.save()
            request.user.save()

            # بروزرسانی سشن کاربر برای حفظ وضعیت ورود
            update_session_auth_hash(request, request.user)

            return redirect('profile')  # Redirect after saving
    else:
        form = CompleteProfileForm(instance=request.user)
    return render(request, 'pannel/profile.html', {'form': form})


@login_required
def rules(request):
    return render(request, 'pannel/Rules/index.html')


@login_required
def about(request):
    return render(request, 'pannel/About/index.html')


@login_required
def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        message = request.POST.get('message')

        # ارسال ایمیل
        # حذف شده

        messages.success(request, 'پیام شما با موفقیت ارسال شد.')
        return redirect('contact')  # بازگشت به صفحه تماس پس از ارسال موفق

    return render(request, 'pannel/contact_us/index.html')


def home(request):
    # تعداد قانونگذاران تأیید شده و رد شده
    approved_lawmakers = assembly.objects.filter(user=request.user, status='approved').count()
    rejected_lawmakers = assembly.objects.filter(user=request.user, status='rejected').count()

    # تعداد اسناد تأیید شده و رد شده
    approved_Document = assembly.objects.filter(user=request.user, status='approved').count()
    rejected_Document = assembly.objects.filter(user=request.user, status='rejected').count()

    # مجموع تأیید شده‌ها و رد شده‌ها
    total_approved = approved_lawmakers + approved_Document
    total_Document = rejected_lawmakers + rejected_Document

    # استفاده از message_type به جای is_public
    notifications = Notification.objects.filter(message_type='public')  # اعلان‌های عمومی

    # تعداد تیکت‌های باز مربوط به کاربر جاری
    tickets_count = Ticket.objects.filter(user=request.user).count()

    return render(request, 'pannel/home/index.html', {
        'approved_lawmakers': total_approved,
        'rejected_lawmakers': total_Document,
        'tickets_count': tickets_count,
        'notifications': notifications,
        'user': request.user
    })