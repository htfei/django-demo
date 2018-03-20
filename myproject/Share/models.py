# /share/models.py

from django.db import models
from datetime import datetime #导入datetime 用于处理上传文件的时间字段


class Upload(models.Model):
    DownloadDocount = models.IntegerField(verbose_name=u"访问次数",default=0)
    #访问该页面的次数 IntegerField 表示整数字段
    code = models.CharField(max_length=8,verbose_name=u"code")
    #唯一标识一个文件 CharField 表示字符串字段
    Datatime = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")
    #Datatime 表示文件上传的时间，其中datetime.now 不能加括号,否则时间
    #就变成了orm生成model的时间,这里一定要注意！！
    path = models.CharField(max_length=32,verbose_name=u"下载路径")
    #path 代表文件存储的路径
    name = models.CharField(max_length=32,verbose_name=u"文件名",default="")
    #name 文件名
    Filesize = models.CharField(max_length=10,verbose_name=u"文件大小")
    # Filesize 文件大小
    PCIP = models.CharField(max_length=32,verbose_name=u"IP地址",default="")
    #PCIP 上传文件的IP

    class Meta():  # Meta 可用于定义数据表名，排序方式等。
        verbose_name="download" #指明一个易于理解和表示的单词形式的对象。
        db_table = "download"#声明数据表的名。

    def __str__(self): #表示在做查询操作时，我们看到的是 name 字段
        return self.name