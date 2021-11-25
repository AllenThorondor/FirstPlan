from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# Create your models here.
class Lane(models.Model):
    flight_name = models.CharField(max_length=20, verbose_name='航空公司', help_text='例如：成都航空')
    flight_num = models.CharField(max_length=10, verbose_name='航班名称', help_text='例如：ZH7847')
    flight_date = models.DateField(auto_now_add=True, verbose_name='航班日期')
    takeoff_time = models.DateTimeField(default=timezone.now, verbose_name='起飞时间')
    arrive_time = models.DateTimeField(default=timezone.now, verbose_name='到达时间')
    provenance = models.CharField(max_length=10, verbose_name='出发地点', help_text='例如：成都双流机场T2航站楼')
    destination = models.CharField(max_length=10, verbose_name='到达地点', help_text='例如：上海虹桥机场T1航站楼')
    note = models.TextField(max_length=1000, verbose_name='记录', help_text='按照书本一点不差的即兴发挥吧')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    picture = models.ImageField(default='lane_pics/default.jpg',
                                upload_to='lane_pics',
                                blank=True,
                                help_text='照片记录')

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('lane-detail', kwargs={'pk':self.pk})

    def get_lane_id(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        super(Lane, self).save(*args, **kwargs)
        if self.picture.path is not "":
            img = Image.open(self.picture.path)
            if img.height > 600 or img.width > 600:
                output_size = (600, 600)
                img.thumbnail(output_size)
                img.save(self.picture.path)
        else:
            pass


def get_flash_id(Lane):
    return Lane.get_lane_id()

class LaneImage(models.Model):
    lane = models.ForeignKey(Lane, default=None, on_delete=models.CASCADE)
    image = models.ImageField(default='flash_pics/default.jpg',
                                upload_to='flash_pics',
                                blank=True)
    def __str__(self):
        return str(self.lane.id)

    def save(self, *args, **kwargs):
        super(Lane, self).save(*args, **kwargs)
        if self.image.path is not "":
            img = Image.open(self.image.path)
            if img.height > 600 or img.width > 600:
                output_size = (600, 600)
                img.thumbnail(output_size)
                img.save(self.image.path)
        else:
            pass

class Flash(models.Model):
    lane = models.ForeignKey(Lane, default=None, on_delete=models.CASCADE,
                            null=True, help_text='对应行程')
    story = models.TextField(null=True, verbose_name='故事', help_text='写下那些故事吧')
    picture = models.ImageField(default='flash_pics/default.jpg',
                                upload_to='flash_pics',
                                blank=True)
    update_time = models.DateTimeField(auto_now_add=True, help_text='更新时间')


    class Meta:
        verbose_name = 'flashs'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.story[:10]


    def save(self, *args, **kwargs):
        super(Flash, self).save(*args, **kwargs)
        if self.picture.path is not "":
            img = Image.open(self.picture.path)

            if img.height > 600 or img.width > 600:
                output_size = (600, 600)
                img.thumbnail(output_size)
                img.save(self.picture.path)
        else:
            pass
