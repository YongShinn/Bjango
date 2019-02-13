from django.contrib import admin
from .models import retailer
from .models import bubble
from .models import items
from .models import orders

# Register your models here.


class RetailerAdmin(admin.ModelAdmin):
    list_display = ('id', 'retail_name', 'retail_url',
                    'retail_fee', 'retail_duration')


class BubbleAdmin(admin.ModelAdmin):
    list_display = ('bubble_RetailID', 'bubble_UserID', 'bubble_amount',
                    'bubble_cartFilled', 'bubble_shipped', 'bubble_start')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('items_RetailerID', 'items_price',
                    'items_name', 'items_category')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('orders_BubbleID', 'orders_UserID',
                    'orders_ItemID', 'orders_TimeDate')


admin.site.register(retailer, RetailerAdmin)
admin.site.register(bubble, BubbleAdmin)
admin.site.register(items, ItemAdmin)
admin.site.register(orders, OrderAdmin)
