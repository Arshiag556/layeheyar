from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserAccount


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
    birth_date = forms.DateField(
        label="تاریخ تولد",
        widget=forms.DateInput(attrs={'type': 'date'})
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

