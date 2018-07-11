from django.db import models
from product.models import Product
# Create your models here.
class Apitest(models.Model):
    #关联产品ID，其中product是应用名,Product是product应用的表名
    product = models.ForeignKey('product.Product',on_delete=models.CASCADE,null=True)
    #流程接口测试场景
    apitestname = models.CharField('流程接口名称',max_length=64)
    #流程接口描述
    apitestdesc = models.CharField('描述',max_length=64,null=True)
    #执行人
    apitester = models.CharField('测试负责人',max_length=16)
    #流程接口测试结果
    apitestresult = models.BooleanField('测试结果')
    #创建时间，自动获取当前时间
    create_time = models.DateTimeField('创建时间',auto_now=True)
    class Meta:
        verbose_name = '流程场景接口'
        verbose_name_plural = '流程场景接口'
    def __str__(self):
        return self.apitestname


class Apistep(models.Model):
    #关联接口ID
    Apitest = models.ForeignKey('Apitest',on_delete=models.CASCADE,)
    #接口标题
    apiname = models.CharField('接口名称',max_length=100)
    #地址
    apiurl = models.CharField('接口地址',max_length=500)
    #请求参数和值
    apiparamvalue = models.CharField('请求参数和值',max_length=800)
    REQUEST_METHOD = (('get','get'),('post','post'),('put','put'),('delete','delete'),('patch','patch'))
    #请求方法
    apimethod = models.CharField('请求方法',choices=REQUEST_METHOD,default='get',max_length=200,null=True)
    #预期接口
    apiresult = models.CharField('预期结果',max_length=1000)
    #测试结果
    apistatus = models.BooleanField('是否通过')
    #创建时间，自动获取
    create_time = models.DateTimeField('创建时间',auto_now=True)
    def __str__(self):
        return self.apiname





