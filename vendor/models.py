from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import OneToOneField

# Create your models here.


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User, related_name='vendor', on_delete=models.CASCADE)
    date_of_birth = models.DateField(default="1990-01-01",blank=True)
    phone_number = models.CharField(max_length=50,blank=True)
    image = models.ImageField(upload_to='uploads/',blank=True,null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.user.username

    def get_balance(self):
        items = self.items.filter(
            vendor_paid=False, order__vendors__in=[self.id])
        return sum((item.product.price * item.quantity) for item in items)

    def get_paid_amount(self):
        items = self.items.filter(
            vendor_paid=True, order__vendors__in=[self.id])
        return sum((item.product.price * item.quantity) for item in items)
