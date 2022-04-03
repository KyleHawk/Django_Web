from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return 'Type name : ' + self.name


class Item(models.Model):
    type = models.ForeignKey(Type, related_name='items',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField(default=100)
    available = models.BooleanField(default=True)
    description = models.CharField(max_length=200,default=True)
    interested = models.PositiveIntegerField(default=0)
    def __str__(self):
        return 'Item name : ' + self.name
    def topup(self):
        self.stock += 200




class Client(User):
    CITY_CHOICES = [
        ('WD','Windsor'),
        ('TO','Toronto'),
        ('CH','Chatham'),
        ('WL','WATERLOO'),]
    shipping_address = models.CharField(max_length=300,null=True)
    city = models.CharField(max_length=2,choices=CITY_CHOICES, default='CH')
    interested_in = models.ManyToManyField(Type)
    phone_number = models.IntegerField(null=True)
    def __str__(self):
        return 'Client name : ' + self.first_name + ' ' + self.last_name


class OrderItem(models.Model):
    item = models.ForeignKey(Item,related_name='item',on_delete=models.CASCADE)
    client = models.ForeignKey(Client,related_name='client',on_delete=models.CASCADE)
    num_of_items = models.IntegerField()
    STATUS_CHOICES = [
        (0,'cancelled order'),
        (1,'placed order'),
        (2,'shipped order'),
        (3,'delivered order'),]
    status = models.IntegerField(choices=STATUS_CHOICES,default=0)
    update_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return  self.item.name + ' order by ' + self.client.first_name

    def total_price(self):
        return self.item.price*self.num_of_items










