from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class retailer(models.Model):
    retail_name = models.CharField(max_length=200)
    retail_url = models.CharField(max_length=200)
    retail_fee = models.DecimalField(max_digits=5, decimal_places=2)
    retail_duration = models.DateTimeField(auto_now_add=True, blank=True)


class bubble(models.Model):
    bubble_RetailID = models.ForeignKey(retailer, on_delete=models.CASCADE)
    bubble_UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    bubble_amount = models.IntegerField()
    bubble_cartFilled = models.BooleanField()
    bubble_shipped = models.BooleanField()
    bubble_start = models.DateTimeField(auto_now_add=True, blank=True)


class items(models.Model):
    items_RetailerID = models.ForeignKey(retailer, on_delete=models.CASCADE)
    items_price = models.DecimalField(max_digits=5, decimal_places=2)
    items_name = models.CharField(max_length=200)
    items_category = models.CharField(max_length=200)


class orders(models.Model):
    orders_BubbleID = models.ForeignKey(bubble, on_delete=models.CASCADE)
    orders_UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    orders_ItemID = models.ForeignKey(items, on_delete=models.CASCADE)
    orders_TimeDate = models.DateTimeField(auto_now_add=True, blank=True)
