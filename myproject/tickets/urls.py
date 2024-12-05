from django.urls import path
from . import views

app_name = 'tickets'
urlpatterns = [
    path('create/', views.create_ticket, name='create_ticket'),
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
]
