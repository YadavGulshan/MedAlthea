from django.db import models
from djangotoolbox.fields import ListField
# Create your models here.

class medicineDetailsModel(models.Model):
    medicine_name = models.CharField(max_length=100)
    medicine_price = models.FloatField(max_length=50)
    medicine_rating = models.FloatField(max_length=5)
    medicine_total_rating = models.IntegerField(max_length=100)
    medicine_noOfTablets = models.IntegerField(max_length=20)





class shopAndOwnerDetails(models.Model):
    owner_first_name = models.CharField(max_length=30)
    owner_last_name = models.CharField(max_length=30)
    owner_email = models.EmailField(max_length=20)
    owner_phone = models.IntegerField(max_length=10)
    shop_name = models.CharField(max_length=15)
    shop_address = models.CharField(max_length=50)
    shope_District = models.CharField(max_length=10)
    shop_state = models.CharField(max_length=10)
    shop_contact = models.IntegerField(max_length=10)
    medicines = ListField()

