from django.db import models

# Create your models here.


class Medical(models.Model):
    medicalId = models.IntegerField(auto_created=True, primary_key=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    pincode = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    phone = models.IntegerField( default=0)
    email = models.EmailField(max_length=100)
    website = models.URLField(max_length=100)
    # An image file with size less than 1MB
    image = models.ImageField(upload_to=f'images/', default='images/default.jpg', max_length=1000)

