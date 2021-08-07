from django.db import models
from products.models import Product
from django.contrib.auth.models import User
# Create your models here.

class BagItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    is_added = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)

class Bag(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(BagItem)

    def get_bag_items(self):
        return self.items.all()