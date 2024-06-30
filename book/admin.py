from django.contrib import admin
from django.utils.html import format_html
from .models import Transaction, Company

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'description', 'main_category', 'sub_category', 'receipts', 'payments', 'file_link')
    search_fields = ('date', 'description', 'main_category', 'sub_category')
    readonly_fields = ('file',)

    def file_link(self, obj):
        if obj.file:
            return format_html('<a href="{}">{}</a>', obj.file.url, obj.file.name)
        else:
            return "No attachment"

    file_link.allow_tags = True
    file_link.short_description = 'File Link'

admin.site.register(Transaction, TransactionAdmin)



class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name',)

admin.site.register(Company, CompanyAdmin)