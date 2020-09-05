from django.db import models
from user.models import User
from product.models import Product
from user.models import User

# Create your models here.
class Order(models.Model):
    NEW = 10
    PAID = 20
    DONE = 30
    STATUSES = (
        (NEW, 'New'), (PAID, 'Paid'), (DONE, 'Done')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUSES, default=NEW)
    billing_name = models.CharField(max_length=100)
    billing_contact = models.CharField(max_length=100)
    billing_address1 = models.CharField(max_length=100)
    billing_address2 = models.CharField(max_length=100, blank=True)
    billing_city = models.CharField(max_length=100)
    billing_zipcode = models.CharField(max_length=100)
    billing_state = models.CharField(max_length=100)
    billing_country = models.CharField(max_length=100)
    shipping_name = models.CharField(max_length=100)
    shipping_contact = models.CharField(max_length=100)
    shipping_address1 = models.CharField(max_length=100)
    shipping_address2 = models.CharField(max_length=100, blank=True)
    shipping_city = models.CharField(max_length=100)
    shipping_zipcode = models.CharField(max_length=100)
    shipping_state = models.CharField(max_length=100)
    shipping_country = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class OrderLine(models.Model):
    NEW = 10
    PROCESSING = 20
    SENT = 30
    CANCELLED = 40
    STATUSES = (
        (NEW, 'New'), (PROCESSING, 'Processing'), [SENT, 'Sent'], (CANCELLED, 'Cancelled')
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='lines')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    vendor = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUSES, default=NEW)
    
