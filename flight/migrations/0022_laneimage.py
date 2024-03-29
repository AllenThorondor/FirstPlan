# Generated by Django 3.2.7 on 2021-11-24 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0021_alter_flash_lane'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaneImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='flash_pics/default.jpg', upload_to='flash_pics')),
                ('lane', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='flight.lane')),
            ],
        ),
    ]
