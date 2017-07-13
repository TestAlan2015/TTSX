from django.db import models

# Create your models here.


class OrderMain(models.Model):
    orderid=models.CharField(max_length=40,primary_key=True)
    ordertime=models.DateTimeField(auto_now_add=True)
    orderuser=models.ForeignKey('ttsxuser.UserInfo')
    orderprice=models.DecimalField(max_digits=6,decimal_places=2)
    class Meta:
        db_table='order_main'

class OrderDetail(models.Model):
    orderid=models.ForeignKey(OrderMain)
    product=models.ForeignKey('ttsxproduct.ProductInfo')
    price=models.DecimalField(max_digits=6,decimal_places=2)
    count=models.IntegerField(default=0)
    localmoney=models.DecimalField(max_digits=6,decimal_places=2)
    class Meta:
        db_table='order_detail'
