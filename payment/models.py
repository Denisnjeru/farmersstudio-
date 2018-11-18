from django.db import models
from cart import cart

# Create your models here.
class Order(models.Model):
    Order_id = models.AutoField(primary_key=True)
    items = models.CharField(max_length=100)
    user = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=3,decimal_places=2)
    number = models.IntegerField()
    confirmed = models.BooleanField(default=False)
    def __str__(self):
        return self.items + self.Order_id