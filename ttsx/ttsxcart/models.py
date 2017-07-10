from django.db import models

# Create your models here.

class CartInfo(models.Model):
    cuser=models.ForeignKey('ttsxuser.UserInfo')
    cproduct=models.ForeignKey('ttsxproduct.ProductInfo')
    count=models.IntegerField()

    class Meta:
        db_table='cart'

