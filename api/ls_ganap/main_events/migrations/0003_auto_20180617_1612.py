# Generated by Django 2.0.5 on 2018-06-17 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_events', '0002_auto_20180617_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
