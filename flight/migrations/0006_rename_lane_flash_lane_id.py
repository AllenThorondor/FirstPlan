# Generated by Django 3.2.7 on 2021-10-25 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0005_lane_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flash',
            old_name='lane',
            new_name='lane_id',
        ),
    ]
