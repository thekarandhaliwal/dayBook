from django import forms
from .models import *
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django import forms
from django.utils.translation import gettext_lazy as _
from .models import *

class TransactionForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    main_category = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    sub_category = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    receipts = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    payments = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.TextInput(attrs={'class': 'form-control'}), label=_('Payments'))
    company = forms.ModelChoiceField(queryset=Company.objects.all(), 
                                     widget=forms.Select(attrs={'class': 'form-control'}),
                                     label=_('Company'))
    currency = forms.ChoiceField(choices=[
        ('USD', _('Dollar (USD)')),
        ('INR', _('Rupee (INR)')),
        ('AED', _('Dirham (AED)')),
        ('EUR', _('Euro (EUR)')),
        ('GBP', _('Pound (GBP)')),
    ], widget=forms.Select(attrs={'class': 'form-control'}))
    file = forms.FileField(widget=forms.ClearableFileInput())

    class Meta:
        model = Transaction
        fields = [
            'date', 'description', 'main_category', 'sub_category', 
            'receipts', 'payments', 'company', 'currency', 'file'
        ]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].initial = timezone.now().date()

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['date'].initial = timezone.now().date()
    #     instance = kwargs.get('instance')
    #     if instance and instance.company:
    #         if 'dubai' in instance.company.name.lower():
    #             self.fields['currency'].initial = 'AED'  # Set Dirham as initial currency
    #         elif 'india' in instance.company.name.lower():
    #             self.fields['currency'].initial = 'INR'  # Set Rupee as initial currency
    #         elif 'usa' in instance.company.name.lower():
    #             self.fields['currency'].initial = 'USD'  # Set Dollar as initial currency
