from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Tag(models.Model):
    name = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name

class Stiver(models.Model):
    item = models.CharField(max_length=20, verbose_name='名称', null=True)
    money = models.FloatField(verbose_name='金额', null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    note = models.TextField(max_length=1000, null=True, verbose_name='记录')
    tags = models.ManyToManyField(Tag)


    def __str__(self):
        return self.item

    def get_absolute_url(self):
        return reverse('stiver-detail', kwargs = {'pk': self.pk})
