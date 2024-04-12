from django.contrib import admin
from .models import WinGiftEmail, Voucher, PrizeProbability
# Register your models here.
from django.db.models import Sum

class PrizeProbabilityAdmin(admin.ModelAdmin):
    list_display = ['money', 'percentage', 'total_percentage']
    search_fields = ['money', 'percentage']
    list_filter = ['percentage', 'money']

    def total_percentage(self, obj):
        total = PrizeProbability.objects.aggregate(Sum('percentage'))['percentage__sum']
        return total if total is not None else 0
    total_percentage.short_description = 'Total Percentage'
    
class WinGiftEmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'prize_won', 'number_selected', 'voucher', 'created')
    search_fields = ['email', 'voucher__code']  # Assuming 'voucher' has a field 'unique_identifier'
    list_filter = ('prize_won', 'created')

class VoucherAdmin(admin.ModelAdmin):
    list_display = ('code', 'created')
    search_fields = ('code',)
    list_filter = ('created',)
    
admin.site.register(WinGiftEmail, WinGiftEmailAdmin)
admin.site.register(Voucher, VoucherAdmin)
admin.site.register(PrizeProbability, PrizeProbabilityAdmin)
