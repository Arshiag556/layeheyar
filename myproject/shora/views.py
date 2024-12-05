from django.shortcuts import render, get_object_or_404, redirect
from .models import Document, assembly
from myapp.models import UserAccount
from .forms import ReceiptUploadForm, assembly_form
from myapp.utils import send_sms_to_admin

def handle_form_submission(request, user, form_class, template_name, documents, success_url, model_class):
    """
    تابع عمومی برای مدیریت فرم‌های مربوط به لایحه‌ها و مستندات.
    """
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            add_measure = form.save(commit=False)
            add_measure.user = user  # اتصال کاربر به فرم
            add_measure.save()

            # ساخت لینک به صفحه جزئیات لایحه در پنل ادمین (بسته به مدل)
            if model_class == Document:
                admin_url = f"http://localhost:8000/admin/myapp/document/{add_measure.id}/"
            elif model_class == assembly:
                admin_url = f"http://localhost:8000/admin/myapp/assembly/{add_measure.id}/"

            # ارسال پیامک به مدیر
            message = f"کاربر {user.name} {user.family} یک لایحه جدید ثبت کرده است:\nعنوان: {add_measure.title}\n \nلینک پنل ادمین {admin_url}"
            send_sms_to_admin(message)

            return redirect(success_url)
        else:
            print("Form errors:", form.errors)
    else:
        form = form_class() if user.is_verified == "4" else None

    return render(request, template_name if form else 'verifyreq.html', {
        'user': user,
        'form': form,
        'documents': documents
    })

def council(request, user_id):
    """
    مدیریت بخش مربوط به شورا.
    """
    user = get_object_or_404(UserAccount, id=user_id)
    documents = Document.objects.filter(user=user)
    return handle_form_submission(
        request=request,
        user=user,
        form_class=ReceiptUploadForm,
        template_name='council.html',
        documents=documents,
        success_url='app1:upload_document_success',
        model_class=Document  # مدل Document را ارسال می‌کنیم
    )


def Assembly(request, user_id):
    """
    مدیریت بخش مربوط به مجمع.
    """
    user = get_object_or_404(UserAccount, id=user_id)
    documents = assembly.objects.filter(user=user)
    return handle_form_submission(
        request=request,
        user=user,
        form_class=assembly_form,
        template_name='assembly.html',
        documents=documents,
        success_url='app1:upload_document_success',
        model_class=assembly  # مدل assembly را ارسال می‌کنیم
    )


def upload_document_success(request):
    """
    نمایش صفحه موفقیت پس از ثبت.
    """
    return render(request, 'success.html')
