# Generated by Django 3.2.7 on 2021-10-30 07:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0011_auto_20211030_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='flash',
            name='update_time',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='更新时间'),
        ),
    ]
