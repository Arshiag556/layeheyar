from django.contrib import admin
from .models import Ticket, TicketResponse

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['title','section', 'user', 'status', 'created_at']
    search_fields = ['title', 'description']

@admin.register(TicketResponse)
class TicketResponseAdmin(admin.ModelAdmin):
    list_display = ['ticket', 'user', 'created_at']
