from django.db import models

# Create your models here.
class Test(models.Model):
    # 类代表数据库中的一张表，此例对应的表名称为 TestModel_test
    # name为字段，字符串型，最长20字节
    # id字段默认自动添加
    name = models.CharField(max_length=20)


class Contact(models.Model):
    name   = models.CharField(max_length=200)
    age    = models.IntegerField(default=0)
    email  = models.EmailField()
    def __unicode__(self):
        return self.name
 
class Tag(models.Model):
    contact = models.ForeignKey(Contact)
    name    = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name