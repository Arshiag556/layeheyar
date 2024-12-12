from django.urls import path
from . import views

app_name = 'tickets'
urlpatterns = [
    path('ticket/create/', views.create_ticket, name='create_ticket'),
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('ticket/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('ticket/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('ticket/admin/<int:ticket_id>/', views.respond_to_ticket, name='respond_to_ticket'),
]
