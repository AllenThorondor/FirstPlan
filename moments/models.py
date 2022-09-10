from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image, ExifTags
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, SmartResize


# Create your models here.
class Collection(models.Model):
    collection_name = models.CharField(max_length=20, verbose_name='专题名称',
                        help_text='例如：时空漫步者，15字以内')
    collection_num = models.CharField(max_length=10, verbose_name='专题编号',
                        help_text='例如：20211121-1')
    date_created = models.DateField(auto_now_add=True, verbose_name='创建日期')
    discription = models.CharField(max_length=220, verbose_name='专题描述',
                        help_text='例如：浔阳江头夜送客，枫叶荻花秋瑟瑟...')
    note = models.TextField(max_length=1000, verbose_name='记录',
                        help_text='按照书本一点不差的即兴发挥吧')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    cover_image = models.ImageField(
                                upload_to='moments_pics',
                                blank=True,
                                help_text='专题封面')
    thumbnail = ImageSpecField(source='cover_image', processors=[SmartResize(600, 600)], format='PNG')

    class Meta:
        verbose_name = '专题图片集'
        verbose_name_plural = verbose_name

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
    thumbnail = ImageSpecField(source='image', processors=[SmartResize(600, 600)], format='PNG')


    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('collection-image-detail', kwargs={'pk':self.pk})

    def save(self, *args, **kwargs):
        super(CollectionImage, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        #相机或手机拍摄图片需要根据exif旋转角度
        try:
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation': break
            exif = dict(img._getexif().items())
            if exif[orientation] == 1:
                pass
            elif exif[orientation] == 2:
                img = img.transpose(PIL.Image.FLIP_LEFT_RIGHT)
            elif exif[orientation] == 3:
                img = img.rotate(180, expand=True)
            elif exif[orientation] == 4:
                img = img.rotate(180).transpose(PIL.Image.FLIP_LEFT_RIGHT)
            elif exif[orientation] == 5:
                img = img.rotate(-90, expand=True).transpose(PIL.Image.FLIP_LEFT_RIGHT)
            elif exif[orientation] == 6:
                img = img.rotate(270, expand=True)
            elif exif[orientation] == 7:
                img = img.rotate(90, expand=True).transpose(PIL.Image.FLIP_LEFT_RIGHT)
            elif exif[orientation] == 8:
                img = img.rotate(90, expand=True)
        except:
          pass

        img.save(self.image.path, quality=100)

class Person(models.Model):
    person_name = models.CharField(max_length=20, verbose_name='人物名称',
                            help_text='例如：本人张楚岚')
    person_num = models.CharField(max_length=10, verbose_name='专题编号',
                            help_text='例如：20211121-1')
    date_created = models.DateField(auto_now_add=True, verbose_name='创建日期')
    discription = models.CharField(max_length=220, verbose_name='专题描述',
                            help_text='例如：一位粉妆玉砌，傲骨英风的翩翩少年')
    note = models.TextField(max_length=1000, verbose_name='记录',
                            help_text='按照书本一点不差的即兴发挥吧')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    cover_image = models.ImageField(
                                upload_to='moments_pics',
                                blank=True,
                                help_text='专题封面')
    thumbnail = ImageSpecField(source='cover_image', processors=[SmartResize(600, 600)], format='PNG')

    class Meta:
        verbose_name = '人物图片集'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.person_name)

    def get_absolute_url(self):
        return reverse('person-detail', kwargs={'pk':self.pk})

    def get_person_id(self):
        return str(self.id)

class PersonImage(models.Model):
    person = models.ForeignKey(Person, default=None, on_delete=models.CASCADE)
    image = models.ImageField(
                                upload_to='moments_pics',
                                blank=True)
    story = models.TextField(null=True, verbose_name='故事', help_text='写下那些故事吧')
    update_time = models.DateTimeField(auto_now_add=True, help_text='更新时间')
    thumbnail = ImageSpecField(source='image', processors=[SmartResize(600, 600)], format='PNG')

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('person-image-detail', kwargs={'pk':self.pk})

    def save(self, *args, **kwargs):
        super(PersonImage, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        #相机或手机拍摄图片需要根据exif旋转角度
        try:
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation': break
            exif = dict(img._getexif().items())
            if exif[orientation] == 1:
                pass
            elif exif[orientation] == 2:
                img = img.transpose(PIL.Image.FLIP_LEFT_RIGHT)
            elif exif[orientation] == 3:
                img = img.rotate(180, expand=True)
            elif exif[orientation] == 4:
                img = img.rotate(180).transpose(PIL.Image.FLIP_LEFT_RIGHT)
            elif exif[orientation] == 5:
                img = img.rotate(-90, expand=True).transpose(PIL.Image.FLIP_LEFT_RIGHT)
            elif exif[orientation] == 6:
                img = img.rotate(270, expand=True)
            elif exif[orientation] == 7:
                img = img.rotate(90, expand=True).transpose(PIL.Image.FLIP_LEFT_RIGHT)
            elif exif[orientation] == 8:
                img = img.rotate(90, expand=True)
        except:
          pass

        img.save(self.image.path, quality=100)

class Event(models.Model):
    event_name = models.CharField(max_length=20, verbose_name='事件名称',
                            help_text='例如：新宿事件，15字以内')
    event_num = models.CharField(max_length=10, verbose_name='专题编号',
                            help_text='例如：20211121-1')
    date_created = models.DateField(auto_now_add=True, verbose_name='创建日期')
    discription = models.CharField(max_length=220, verbose_name='专题描述',
                            help_text='例如：永和九年，岁在癸丑，暮春之初...')
    note = models.TextField(max_length=1000, verbose_name='记录',
                            help_text='按照书本一点不差的即兴发挥吧')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    cover_image = models.ImageField(
                                upload_to='moments_pics',
                                blank=True,
                                help_text='专题封面')
    thumbnail = ImageSpecField(source='cover_image', processors=[SmartResize(600, 600)], format='PNG')

    class Meta:
        verbose_name = '事件图片集'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.event_name)

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk':self.pk})

    def get_event_id(self):
        return str(self.id)

class EventImage(models.Model):
    event = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
    image = models.ImageField(
                                upload_to='moments_pics',
                                blank=True)
    story = models.TextField(null=True, verbose_name='故事', help_text='写下那些故事吧')
    update_time = models.DateTimeField(auto_now_add=True, help_text='更新时间')
    thumbnail = ImageSpecField(source='image', processors=[SmartResize(600, 600)], format='PNG')

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('event-image-detail', kwargs={'pk':self.pk})

    def save(self, *args, **kwargs):
        super(EventImage, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        #相机或手机拍摄图片需要根据exif旋转角度
        try:
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation': break
            exif = dict(img._getexif().items())
            if exif[orientation] == 1:
                pass
            elif exif[orientation] == 2:
                img = img.transpose(PIL.Image.FLIP_LEFT_RIGHT)
            elif exif[orientation] == 3:
                img = img.rotate(180, expand=True)
            elif exif[orientation] == 4:
                img = img.rotate(180).transpose(PIL.Image.FLIP_LEFT_RIGHT)
            elif exif[orientation] == 5:
                img = img.rotate(-90, expand=True).transpose(PIL.Image.FLIP_LEFT_RIGHT)
            elif exif[orientation] == 6:
                img = img.rotate(270, expand=True)
            elif exif[orientation] == 7:
                img = img.rotate(90, expand=True).transpose(PIL.Image.FLIP_LEFT_RIGHT)
            elif exif[orientation] == 8:
                img = img.rotate(90, expand=True)
        except:
          pass

        img.save(self.image.path, quality=100)
