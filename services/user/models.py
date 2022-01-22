from django.db import models

# Create your models here.
class UserDetails(models.Model):
    user_first_name = models.CharField(max_length=10)
    user_last_name = models.CharField(max_length=10)
    user_phone_number = models.IntegerField(max_length=10)
    user_email = models.EmailField(max_length=20)
    user_password = models.CharField(max_length=20)
    user_join_on = models.DateTimeField(auto_now_add=True)