from django.conf import settings
from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
    ('I', 'iphone'),
    ('Iw', 'i-watch'),
    ('A', 'airPods') 
)

SKIN_CHOICES = (
    ('BK', 'Black'),
    ('RD', 'Red'),
    ('WH', 'White'),
    ('PK', 'Pink') 
)

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    skin = models.CharField(choices=SKIN_CHOICES, max_length=2)
    
    def __str__(self):
        return self.title

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
