from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# Create your models here.
class Collection(models.Model):
    collection_name = models.CharField(max_length=20, verbose_name='专题名称', help_text='例如：时空漫步者')
    collection_num = models.CharField(max_length=10, verbose_name='专题编号', help_text='例如：20211121-1')
    date_created = models.DateField(auto_now_add=True, verbose_name='创建日期')
    discription = models.CharField(max_length=220, verbose_name='专题描述', help_text='例如：')
    note = models.TextField(max_length=1000, verbose_name='记录', help_text='按照书本一点不差的即兴发挥吧')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    cover_image = models.ImageField(
                                upload_to='moments_pics',
                                blank=True,
                                help_text='专题封面')

    def __str__(self):
        return str(self.collection_name)

    def get_absolute_url(self):
        return reverse('collection-detail', kwargs={'pk':self.pk})

    def get_collection_id(self):
        return str(self.id)


class CollectionImage(models.Model):
    collection = models.ForeignKey(Collection, default=None, on_delete=models.CASCADE)
    image = models.ImageField(
                                upload_to='moments_pics',
                                blank=True)
    story = models.TextField(null=True, verbose_name='故事', help_text='写下那些故事吧')
    update_time = models.DateTimeField(auto_now_add=True, help_text='更新时间')

    class Meta:
        verbose_name = '专题图片集'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.Collection.id)


class Person(models.Model):
    person_name = models.CharField(max_length=20, verbose_name='人物名称', help_text='例如：本人张楚岚')
    person_num = models.CharField(max_length=10, verbose_name='专题编号', help_text='例如：20211121-1')
    date_created = models.DateField(auto_now_add=True, verbose_name='创建日期')
    discription = models.CharField(max_length=220, verbose_name='专题描述', help_text='例如：')
    note = models.TextField(max_length=1000, verbose_name='记录', help_text='按照书本一点不差的即兴发挥吧')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    cover_image = models.ImageField(
                                upload_to='moments_pics',
                                blank=True,
                                help_text='专题封面')

    def __str__(self):
        return str(self.person_name)

    def get_absolute_url(self):
        return reverse('collection-detail', kwargs={'pk':self.pk})

    def get_person_id(self):
        return str(self.id)


class PersonImage(models.Model):
    person = models.ForeignKey(Person, default=None, on_delete=models.CASCADE)
    image = models.ImageField(
                                upload_to='moments_pics',
                                blank=True)
    story = models.TextField(null=True, verbose_name='故事', help_text='写下那些故事吧')
    update_time = models.DateTimeField(auto_now_add=True, help_text='更新时间')

    class Meta:
        verbose_name = '专题图片集'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.Person.id)

class Event(models.Model):
    event_name = models.CharField(max_length=20, verbose_name='事件名称', help_text='例如：新宿事件')
    event_num = models.CharField(max_length=10, verbose_name='专题编号', help_text='例如：20211121-1')
    date_created = models.DateField(auto_now_add=True, verbose_name='创建日期')
    discription = models.CharField(max_length=220, verbose_name='专题描述', help_text='例如：')
    note = models.TextField(max_length=1000, verbose_name='记录', help_text='按照书本一点不差的即兴发挥吧')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    cover_image = models.ImageField(
                                upload_to='moments_pics',
                                blank=True,
                                help_text='专题封面')

    def __str__(self):
        return str(self.event_name)

    def get_absolute_url(self):
        return reverse('collection-detail', kwargs={'pk':self.pk})

    def get_event_id(self):
        return str(self.id)


class EventImage(models.Model):
    event = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
    image = models.ImageField(
                                upload_to='moments_pics',
                                blank=True)
    story = models.TextField(null=True, verbose_name='故事', help_text='写下那些故事吧')
    update_time = models.DateTimeField(auto_now_add=True, help_text='更新时间')

    class Meta:
        verbose_name = '专题图片集'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.Event.id)
