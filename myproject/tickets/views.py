from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketForm, TicketResponseForm,AdminTicketForm
from myapp.utils import new_ticket_notif
from django.contrib.auth.decorators import user_passes_test



@login_required
def create_ticket(request, ):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            # ارسال پیامک به مدیر
            message = f"کاربر  تیکت جدید ایجاد کرد"
            new_ticket_notif(message)
            return redirect('tickets:ticket_list')
    else:
        form = TicketForm()
    return render(request, 'create_ticket.html', {'form': form})

@login_required
def ticket_list(request):
    tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'ticket_list.html', {'tickets': tickets})




@login_required
def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    # بررسی اینکه فقط کاربر مالک تیکت یا ادمین‌ها به آن دسترسی دارند
    if request.user != ticket.user and not request.user.is_staff:
        return redirect('tickets:ticket_list')

    if request.method == 'POST':
        form = TicketResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.ticket = ticket
            response.user = request.user  # می‌تواند ادمین یا کاربر معمولی باشد
            response.save()
            return redirect('tickets:ticket_detail', ticket_id=ticket_id)
    else:
        form = TicketResponseForm()

    return render(request, 'ticket_detail.html', {
        'ticket': ticket,
        'form': form

    })

# بررسی اینکه کاربر ادمین باشد
def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin)
def admin_dashboard(request):
    tickets = Ticket.objects.all().order_by('-created_at')  # مرتب‌سازی بر اساس تاریخ ایجاد
    context = {
        'tickets': tickets,
    }
    return render(request, 'admin_dashboard.html', context)

@user_passes_test(is_admin)
def respond_to_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == 'POST':
        # فرم پاسخ ادمین
        response_form = TicketResponseForm(request.POST)
        # فرم تغییر وضعیت
        status_form = AdminTicketForm(request.POST)

        if response_form.is_valid() and status_form.is_valid():
            # ذخیره پاسخ
            response = response_form.save(commit=False)
            response.ticket = ticket
            response.user = request.user
            response.save()

            # ذخیره تغییر وضعیت
            ticket.status = status_form.cleaned_data['status']
            ticket.save()

            print("Ticket response and status saved successfully")
            return redirect('tickets:respond_to_ticket', ticket_id=ticket_id)

    else:
        response_form = TicketResponseForm()
        status_form = AdminTicketForm()

    return render(request, 'respond_ticket.html', {
        'ticket': ticket,
        'response_form': response_form,
        'status_form': status_form,
    })

def admin_dashboard(request):
    section = request.GET.get('section', 'all')

    if section == 'all':
        tickets = Ticket.objects.all()
    else:
        tickets = Ticket.objects.filter(section=section)

    return render(request, 'admin_dashboard.html', {'tickets': tickets})