from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Medical(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    medicalId = models.AutoField(auto_created=True,serialize=False, verbose_name='ID', primary_key=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    pincode = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    phone = PhoneNumberField()
    email = models.EmailField(max_length=100)
    website = models.URLField(max_length=100, blank=True)
    # An image file with size less than 1MB
    image = models.ImageField(upload_to=f'images/', default='images/default.jpg', max_length=1000)

class Medicine(models.Model):
    medicalId = models.ForeignKey('Medical', on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()