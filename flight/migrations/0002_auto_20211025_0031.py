# Generated by Django 3.2.7 on 2021-10-24 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lane',
            name='picture',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='lane',
            name='destination',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='lane',
            name='provenance',
            field=models.CharField(max_length=10),
        ),
    ]
