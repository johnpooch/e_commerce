from django.contrib import admin
from .models import Purchase, PurchaseLineItem

# Register your models here.

class PurchaseLineAdminInline(admin.TabularInline):
    model = PurchaseLineItem
    
class PurchaseAdmin(admin.ModelAdmin):
    inlines = (PurchaseLineAdminInline, )
    
admin.site.register(Purchase, PurchaseAdmin)