from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Articles(models.Model):
     title = models.CharField(max_length=128,verbose_name="文章标题")
     author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="文章作者")
     img = models.ImageField(upload_to="",verbose_name="文章配图")
     abstract = models.TextField(verbose_name="文章摘要")
     content = models.TextField(verbose_name="文章内容")
     visited = models.IntegerField(verbose_name="文章访问量")
     created_at = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
     modified_at = models.DateTimeField(auto_now=True,verbose_name="修改时间")

    
    