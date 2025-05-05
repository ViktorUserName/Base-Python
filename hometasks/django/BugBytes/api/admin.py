from django.contrib import admin

from api.models import OrderItem, Order, User


class OrderItemInline(admin.TabularInline):
    model = OrderItem  

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemInline
    ]
    
admin.site.register(Order, OrderAdmin)
admin.site.register(User)
