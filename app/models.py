from django.db import models
from django.db.models import Sum, Avg, Max, Min


class Product(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    ordered_at = models.DateTimeField(auto_now_add=True)

    #total_price = Product.objects.annotate(order__price=Sum('price'))


class Category(models.Model):
    name = models.CharField(max_length=100)
