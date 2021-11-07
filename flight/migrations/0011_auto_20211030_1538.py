# Generated by Django 3.2.7 on 2021-10-30 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flight', '0010_auto_20211026_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='flash',
            name='story',
            field=models.TextField(help_text='写下那些故事吧', null=True),
        ),
        migrations.AlterField(
            model_name='flash',
            name='lane',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flight.lane'),
        ),
        migrations.AlterField(
            model_name='flash',
            name='picture',
            field=models.ImageField(blank=True, default='flash_pics/default.jpg', upload_to='flash_pics'),
        ),
        migrations.AlterField(
            model_name='lane',
            name='arrive_time',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='到达时间'),
        ),
        migrations.AlterField(
            model_name='lane',
            name='author',
            field=models.ForeignKey(help_text='作者', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lane',
            name='destination',
            field=models.CharField(help_text='到达地点', max_length=10),
        ),
        migrations.AlterField(
            model_name='lane',
            name='flight_date',
            field=models.DateField(auto_now_add=True, help_text='航班日期'),
        ),
        migrations.AlterField(
            model_name='lane',
            name='flight_name',
            field=models.CharField(help_text='航空公司', max_length=20),
        ),
        migrations.AlterField(
            model_name='lane',
            name='flight_num',
            field=models.CharField(help_text='航班名称', max_length=10),
        ),
        migrations.AlterField(
            model_name='lane',
            name='note',
            field=models.TextField(help_text='记录', max_length=1000),
        ),
        migrations.AlterField(
            model_name='lane',
            name='picture',
            field=models.ImageField(blank=True, default='lane_pics/default.jpg', help_text='照片记录', upload_to='lane_pics'),
        ),
        migrations.AlterField(
            model_name='lane',
            name='provenance',
            field=models.CharField(help_text='出发地点', max_length=10),
        ),
        migrations.AlterField(
            model_name='lane',
            name='takeoff_time',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='起飞时间'),
        ),
    ]
