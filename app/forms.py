# forms.py
from django import forms
from .models import WinGiftEmail, Voucher

class WinGiftEmailForm(forms.ModelForm):
    voucher = forms.CharField(widget=forms.TextInput())

    
    class Meta:
        model = WinGiftEmail
        fields = ['email', 'voucher']
        
    def clean_voucher(self):
        code = self.cleaned_data['voucher']
        voucher, created = Voucher.objects.get_or_create(code=code)
        if not created:
            raise forms.ValidationError("Voucher code already exists")
        return voucher
