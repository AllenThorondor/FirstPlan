# Generated by Django 3.2.7 on 2021-11-24 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0003_auto_20211124_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='plan_state',
            field=models.IntegerField(default=0, null=True, verbose_name='任务状态'),
        ),
    ]