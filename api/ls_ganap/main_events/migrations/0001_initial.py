# Generated by Django 2.0.5 on 2018-06-20 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_accepted', models.BooleanField(default=False)),
                ('poster_url', models.URLField()),
                ('outside_venue_name', models.CharField(blank=True, max_length=200)),
                ('is_premium', models.BooleanField(default=False)),
                ('event_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='EventHost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('color', models.CharField(max_length=20)),
                ('logo_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='EventHostSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_host_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_events.EventHost')),
            ],
        ),
        migrations.CreateModel(
            name='FollowedEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TagSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_events.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='TagToEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_events.Event')),
                ('tag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_events.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='host_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_events.EventHost'),
        ),
        migrations.AddField(
            model_name='event',
            name='venue_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_events.Venue'),
        ),
    ]
