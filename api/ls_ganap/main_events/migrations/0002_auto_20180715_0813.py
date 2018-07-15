# Generated by Django 2.0.5 on 2018-07-15 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
