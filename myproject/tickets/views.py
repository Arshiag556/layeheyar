from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketForm, TicketResponseForm

@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
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