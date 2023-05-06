from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name='客户名称', help_text='客户名称全称')
    address = models.CharField(max_length=100, blank=True, verbose_name='地址', help_text='客户办公地址')
    content = models.TextField(verbose_name='内容', help_text='客户情况简述')
    date_posted = models.DateTimeField(default=timezone.now, verbose_name='发布时间')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='作者')
    tags = TaggableManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company-detail', kwargs = {'pk': self.pk})

class CompanyUpdate(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    story = models.TextField(null=True, verbose_name='故事', help_text='项目进展更新')

    def __str__(self):
        return self.company.name
