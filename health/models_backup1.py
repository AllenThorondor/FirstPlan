from django.db import models, connection, DatabaseError, transaction
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import pytesseract
from PIL import Image, ImageDraw



# Create your models here.
class Record(models.Model):
    date = models.CharField(max_length=10, verbose_name='日期', null=True)
    score = models.CharField(max_length=10, verbose_name='睡眠分数', null=True)
    get_bed_time = models.CharField(max_length=10, verbose_name='入睡时间', null=True)
    get_up_time = models.CharField(max_length=10, verbose_name='苏醒时间', null=True)
    total_time = models.CharField(max_length=10, verbose_name='总睡眠时长', null=True)
    deep_time = models.CharField(max_length=10, verbose_name='深睡时长', null=True)
    light_time = models.CharField(max_length=10, verbose_name='浅睡时长', null=True)
    dream_time = models.CharField(max_length=10, verbose_name='做梦时长', null=True)
    sober_time = models.CharField(max_length=10, verbose_name='清醒时长', null=True)
    snap_time = models.CharField(max_length=10, verbose_name='零星小睡', null=True)
    breath_score = models.CharField(max_length=10, verbose_name='呼吸质量', null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者', null=True)
    picture = models.ImageField(upload_to='health_pics',
                                blank=True,
                                help_text='待解析图片')

    def save(self, *args, **kwargs):
        super(Record, self).save(*args, **kwargs)

        coord = {'date':(450, 150, 670, 206), 'score':(450, 630, 670, 790),
         'get_bed_time': (5, 1080, 120, 1140), 'get_up_time':(1010, 1080, 1120, 1140),
         'total_time':(400, 1230, 670, 1290), 'deep_time': (70, 1400, 290, 1470),
         'light_time': (600, 1400, 850, 1470), 'dream_time': (70, 1570, 290, 1640),
         'sober_time': (600, 1570, 850, 1640), 'snap_time': (760, 1860, 880, 1920),
         'breath_score': (840, 2090, 904, 2160)}

        img = Image.open(self.picture.path).convert('L')

        def tess_trans(coord_tuple):
            drawing_object = ImageDraw.Draw(img)
            drawing_object.rectangle(coord_tuple, fill=None, outline="red")
            little_sign = img.crop(coord_tuple)
            temp_value = pytesseract.image_to_string(little_sign, lang='chi_sim')
            if temp_value == '':
                temp_value = pytesseract.image_to_string(little_sign, config='--psm 6 --oem 3 -c tessedic_char_whitelist=0123456789')

            return ''.join(temp_value.split())


        for key, value in coord.items():
            Record.objects.raw(f"""
                        UPDATE health_record SET {key} = ? WHERE id = ?
            """, (tess_trans(value), self.id))

        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
        img.save(self.picture.path)
