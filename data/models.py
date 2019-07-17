from django.db import models

# Create your models here.
class Test(models.Model):
    number = models.CharField(verbose_name="数据测试",max_length=12)
    def __str__(self):
        return self.number
class BuyUser(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    def __str__(self):
        return self.username

class SellUser(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    def __str__(self):
        return self.username

class Admin(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    def __str__(self):
        return self.username

class Cartype(models.Model):
    type = models.CharField(verbose_name="商品类别",max_length=32)
    def __str__(self):
        return self.type

class Carfirm(models.Model):
    firm = models.CharField(verbose_name="商品厂商",max_length=32)
    def __str__(self):
        return self.firm

class CarInfo(models.Model):
    carname = models.CharField(verbose_name="汽车名称",max_length=32)
    carfirm = models.ForeignKey(verbose_name="所属经销商",to=Carfirm,on_delete=models.CASCADE)
    cartype = models.ForeignKey(verbose_name="所属类别",to=Cartype,on_delete=models.CASCADE)
    carsell = models.CharField(verbose_name="车主姓名",max_length=32)
    carphone = models.CharField(verbose_name="车主电话",max_length=32)
    carsize = models.CharField(verbose_name="车辆价格",max_length=32)
    carbetter = models.CharField(verbose_name="优惠信息",max_length=32)
    carother = models.CharField(verbose_name="车辆里程",max_length=32)
    carage = models.CharField(verbose_name="车辆车龄",max_length=32,default=None)
    catstatus = models.CharField(verbose_name="成交状态",
                                 choices=(('待支付','待支付'),('已支付','已支付')),max_length=32, default="待支付")

    def __str__(self):
        return self.carname

class UserManager(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    usertype = models.CharField(verbose_name='用户类型', max_length=32)
    def __str__(self):
        return self.username

class OrderManager(models.Model):
    carname = models.CharField(verbose_name="汽车名称",max_length=32)
    carstatus = models.CharField(verbose_name="订单状态",max_length=32)
    def __str__(self):
        return self.carname