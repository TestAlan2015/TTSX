from django.db import models

# Create your models here.

class UserInfo(models.Model):
    uname=models.CharField(max_length=20)
    upassword=models.CharField(max_length=40)
    umail=models.CharField(max_length=40)
    uphone=models.CharField(max_length=20)
    ureveiver=models.CharField(max_length=20)
    ucode=models.CharField(max_length=10)
    address=models.CharField(max_length=100)

    class Meta:
        db_table='user'
