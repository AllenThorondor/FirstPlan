# Generated by Django 3.2.7 on 2021-10-30 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20211030_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(help_text='内容', verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name='标题'),
        ),
    ]
