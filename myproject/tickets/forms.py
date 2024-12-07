from django import forms
from .models import Ticket, TicketResponse

class TicketForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        label="عنوان تیکت",

    )
    section = forms.ChoiceField(
        required=True,
        label="بخش تیکت",
        choices=[
            ('support', 'پشتیبانی'),
            ('sales', 'فروش'),
            ('technical', 'فنی')
        ],

    )


    description = forms.CharField(
            label="توضیحات تیکت",
            widget=forms.Textarea(attrs={
                'class': 'form-control',  # Optional: Add CSS classes for styling
                'rows': 5,  # Optional: Define the number of rows
                'placeholder': 'لطفاً توضیحات تیکت خود را وارد کنید...'  # Optional: Add a placeholder
            }))

    class Meta:
        model = Ticket
        fields = ['title','section', 'description']


class TicketResponseForm(forms.ModelForm):
    message = forms.CharField(
        required=True,
        label="پیام",
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40})  # Example of adding a widget
    )

    class Meta:
        model = TicketResponse
        fields = ['message']