from django.db import models
from django.core.validators import MinValueValidator
from user.models import User
from product.models import Product

# Create your models here.
class Cart(models.Model):
    OPEN = 10
    SUBMITTED = 20
    STATUSES = (
        (OPEN, 'Open'), (SUBMITTED, 'Submitted'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE,
        null=True, blank=True, related_name='cart')
    status = models.IntegerField(choices=STATUSES, default=OPEN)

    def is_empty(self):
        return self.cart_item.all().count() == 0

    def count(self):
        return sum(i.quantity for i in self.cart_item.all())

class CartLine(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
