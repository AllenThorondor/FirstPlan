# Generated by Django 3.2.7 on 2021-11-29 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moments', '0003_event_eventimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventimage',
            old_name='person',
            new_name='event',
        ),
    ]
