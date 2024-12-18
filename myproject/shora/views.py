from django.shortcuts import render, get_object_or_404, redirect
from .models import Document, assembly
from myapp.models import UserAccount
from .forms import ReceiptUploadForm, assembly_form
from myapp.utils import send_sms_to_admin
from django.contrib import messages
from django.urls import reverse


def handle_form_submission(request, user, form_class, template_name, documents, success_url, model_class, fee_amount):
    """
    Handle form submission for both Document and Assembly.
    """
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            required_amount = fee_amount  # Dynamic fee
            if user.balance >= required_amount:
                user.balance -= fee_amount
                user.save()

                add_measure = form.save(commit=False)
                add_measure.user = user
                add_measure.save()

                # Dynamic admin URL
                admin_url = reverse(f'admin:{model_class._meta.app_label}_{model_class._meta.model_name}_change',
                                    args=[add_measure.id])
                admin_url = request.build_absolute_uri(admin_url)

                message = f"کاربر {user.name} {user.family} یک لایحه جدید ثبت کرده است:\nعنوان: {add_measure.title}\n\nلینک پنل ادمین {admin_url}"
                send_sms_to_admin(message)

                messages.success(request, "لایحه با موفقیت ثبت شد!")
                return redirect(success_url)
            else:
                messages.error(request, "موجودی کافی برای ثبت لایحه ندارید. لطفاً حساب خود را شارژ کنید.")
                return redirect('submit_payment')  # Redirect to payment page
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
    Manage council-related document submissions.
    """
    user = get_object_or_404(UserAccount, id=user_id)
    documents = Document.objects.filter(user=user)
    fee_amount = 500000  # Fee amount for Document submission
    return handle_form_submission(
        request=request,
        user=user,
        form_class=ReceiptUploadForm,
        template_name='council.html',
        documents=documents,
        success_url='app1:upload_document_success',
        model_class=Document,
        fee_amount=fee_amount
    )


def Assembly(request, user_id):
    """
    Manage assembly-related document submissions.
    """
    user = get_object_or_404(UserAccount, id=user_id)
    documents = assembly.objects.filter(user=user)
    fee_amount = 500000  # Fee amount for Assembly submission
    return handle_form_submission(
        request=request,
        user=user,
        form_class=assembly_form,
        template_name='assembly.html',
        documents=documents,
        success_url='app1:upload_document_success',
        model_class=assembly,
        fee_amount=fee_amount
    )


def upload_document_success(request):
    """
    Display success page after successful document upload.
    """
    return render(request, 'success.html')
