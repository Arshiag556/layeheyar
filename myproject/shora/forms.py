from django import forms
from .models import Document,assembly

class ReceiptUploadForm(forms.ModelForm):
    title = forms.CharField(
        max_length=255,
        required=True,
        label="عنوان لایحه",
        widget=forms.TextInput(attrs={'placeholder': 'عنوان لایحه را وارد کنید'})
    )

    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'متن کامل لایحه'}),
        required=False,
        label="متن لایحه"
    )
    subject = forms.ChoiceField(
        choices=Document.SUBJECT_CHOICES,
        required=True,
        label="موضوع"
    )

    receipt_image = forms.FileField(
        required=True,
        label="آپلود تصویر رسید",
        widget=forms.ClearableFileInput(attrs={'accept': 'image/jpeg, image/png, image/gif'})
    )

    Letterattachment = forms.FileField(
        required=False,
        label="ضمیمه لایحه",
        widget=forms.ClearableFileInput(attrs={'accept': 'application/pdf, .docx'})
    )


    class Meta:
        model = Document
        fields = ['title','subject', 'text', 'receipt_image' ,'Letterattachment']

class assembly_form(forms.ModelForm):
    title = forms.CharField(
        max_length=255,
        required=True,
        label="عنوان لایحه",
        widget=forms.TextInput(attrs={'placeholder': 'عنوان لایحه را وارد کنید'})
    )

    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'متن کامل لایحه'}),
        required=False,
        label="متن لایحه"
    )
    subject = forms.ChoiceField(
        choices=Document.SUBJECT_CHOICES,
        required=True,
        label="موضوع"
    )

    receipt_image = forms.FileField(
        required=True,
        label="آپلود تصویر رسید",
        widget=forms.ClearableFileInput(attrs={'accept': 'image/jpeg, image/png, image/gif'})
    )

    Letterattachment = forms.FileField(
        required=False,
        label="ضمیمه لایحه",
        widget=forms.ClearableFileInput(attrs={'accept': 'application/pdf, .docx'})
    )


    class Meta:
        model = assembly
        fields = ['title','subject', 'text', 'receipt_image' ,'Letterattachment']
