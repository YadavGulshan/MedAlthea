# pylint: disable=missing-module-docstring
#
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/pharmaService > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class Medical(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    medicalId = models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)
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
    image = models.ImageField(upload_to='images/')
    """
     To get this image stored, Note to use api endpoint.

     I wasted hours wonder why the hell I'm unable to get the stored image...
     But when I later tried https://127.0.0.1:8000/api/media/images/your-image.jpg
    """


class Medicine(models.Model):
    medicalId = models.ForeignKey('Medical', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
