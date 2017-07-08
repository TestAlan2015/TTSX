#coding=utf-8
from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class TypeInfo(models.Model):
    ttitle=models.CharField(max_length=30)
    isDelete=models.BooleanField(default=False)

    def __str__(self):
        return self.ttitle.encode('utf-8')
    class Meta:
        db_table='type'

class ProductInfo(models.Model):
    pname=models.CharField(max_length=20)
    pimage=models.ImageField(upload_to='goods')
    pprice=models.DecimalField(max_digits=5,decimal_places=2)
    pclick = models.IntegerField(default=0)
    punit=models.CharField(max_length=20)
    pcomment=models.IntegerField(default=0)
    psubtitle=models.CharField(max_length=200)
    pkucun=models.IntegerField(default=100)
    pdescription=HTMLField()
    ptype=models.ForeignKey('TypeInfo')

    class Meta:
        db_table='product'

#(0,'','',,0,'500g',0,'经典36#果 单果重约90-100g',100,'<ul class=\"parameter2 p-parameter-list\" style=\"margin: 0px; padding: 20px 0px 15px; list-style: none; overflow: hidden; color: #666666; font-family: tahoma, arial, \'Microsoft YaHei\', \'Hiragino Sans GB\', u5b8bu4f53, sans-serif; line-height: 18px;\">\r\n<li style=\"margin: 0px 0px 5px; padding: 0px 0px 0px 42px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; width: 200px; float: left;\" title=\"佳沛佳沛新西兰绿奇异果 12个\">商品名称：佳沛佳沛新西兰绿奇异果 12个</li>\r\n<li style=\"margin: 0px 0px 5px; padding: 0px 0px 0px 42px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; width: 200px; float: left;\" title=\"3976754\">商品编号：3976754</li>\r\n<li style=\"margin: 0px 0px 5px; padding: 0px 0px 0px 42px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; width: 200px; float: left;\" title=\"1.36kg\">商品毛重：1.36kg</li>\r\n<li style=\"margin: 0px 0px 5px; padding: 0px 0px 0px 42px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; width: 200px; float: left;\" title=\"新西兰\">商品产地：新西兰</li>\r\n<li style=\"margin: 0px 0px 5px; padding: 0px 0px 0px 42px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; width: 200px; float: left;\" title=\"1kg以下\">重量：1kg以下</li>\r\n<li style=\"margin: 0px 0px 5px; padding: 0px 0px 0px 42px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; width: 200px; float: left;\" title=\"进口\">国产/进口：进口</li>\r\n<li style=\"margin: 0px 0px 5px; padding: 0px 0px 0px 42px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; width: 200px; float: left;\" title=\"绿果\">分类：绿果</li>\r\n<li style=\"margin: 0px 0px 5px; padding: 0px 0px 0px 42px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; width: 200px; float: left;\" title=\"简装\">包装：简装</li>\r\n<li style=\"margin: 0px 0px 5px; padding: 0px 0px 0px 42px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; width: 200px; float: left;\" title=\"新西兰\">原产地：新西兰</li>\r\n</ul>',1),
