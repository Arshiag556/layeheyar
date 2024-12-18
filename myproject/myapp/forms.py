from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserAccount
from persiantools.jdatetime import JalaliDate
from .models import Payment


class SignupForm(UserCreationForm):
    name = forms.CharField(label='نام')
    family = forms.CharField(label='نام خانوادگی')
    phone_number = forms.CharField(max_length=15, label='شماره تلفن')
    password1 = forms.CharField(widget=forms.PasswordInput(), label='پسورد')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='تکرار پسورد')

    class Meta:
        model = UserAccount
        fields = ('name', 'family', 'phone_number', 'password1', 'password2')

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if UserAccount.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("A user with this phone number already exists.")
        return phone_number


class PhoneVerificationForm(forms.Form):
    verification_code = forms.CharField(max_length=6, required=True, label='کد تأیید')


class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=15, label="شماره تلفن")
    password = forms.CharField(widget=forms.PasswordInput, label="رمز عبور")

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        # اگر نیاز به اعتبارسنجی خاصی دارید، اینجا اضافه کنید
        return phone_number


from django import forms
from django.contrib.auth.models import User


class CompleteProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(label="پروفایل")
    # فیلدی برای انتخاب تاریخ میلادی
    date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
        label="تاریخ میلادی"
    )

    id_card = forms.ImageField(label=" کارت ملی")
    selfie = forms.ImageField(label="عکس سلفی با کارت ملی")
    national_code = forms.CharField(label="کد ملی")

    # اضافه کردن فیلدهای پسورد
    password = forms.CharField(
        label="رمز عبور جدید",
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور جدید'}),
        required=False
    )
    password_confirm = forms.CharField(
        label="تایید رمز عبور",
        widget=forms.PasswordInput(attrs={'placeholder': 'تایید رمز عبور'}),
        required=False
    )

    class Meta:
        model = UserAccount  # یا User اگر از مدل پیش‌فرض Django استفاده می‌کنید
        fields = (
            'name', 'family', 'phone_number', 'birth_date', 'profile_picture', 'id_card', 'selfie', 'national_code',
            'password', 'password_confirm'
        )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password != password_confirm:
            raise forms.ValidationError("رمز عبور و تایید رمز عبور با هم تطابق ندارند.")

        return cleaned_data

    def clean_date(self):
        """
        این متد داده‌های واردشده را می‌گیرد و به شمسی تبدیل می‌کند.
        """
        date = self.cleaned_data['date']
        # تبدیل تاریخ میلادی به شمسی
        shamsi_date = JalaliDate.from_gregorian(gregorian_date=date).strftime('%Y/%m/%d')
        return shamsi_date





class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'card_number','receipt_image']  # مشخصات فرم
        labels = {
            'amount': 'مبلغ پرداخت',  # تغییر نام فیلد به فارسی
            'card_number':'شماره کارت',
            'receipt_image': 'تصویر رسید پرداخت',  # تغییر نام فیلد به فارسی
        }


    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount < 500000:
            raise forms.ValidationError('مبلغ پرداخت باید حداقل 500,000 تومان باشد.')
        return amount
