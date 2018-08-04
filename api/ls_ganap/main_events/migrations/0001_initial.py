# Generated by Django 2.0.5 on 2018-08-04 14:23

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import main_events.models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', main_events.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('logo_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=200)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('recurrence_bool', models.BooleanField(default=False, help_text='Is the event recurring?')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_accepted', models.BooleanField(default=False)),
                ('poster_url', models.URLField()),
                ('outside_venue_name', models.CharField(blank=True, max_length=200)),
                ('is_premium', models.BooleanField(default=False)),
                ('event_url', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventHost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('abbreviation', models.CharField(blank=True, max_length=10)),
                ('description', models.TextField()),
                ('accredited', models.BooleanField(default=False)),
                ('color', models.CharField(max_length=20)),
                ('logo_url', models.URLField()),
                ('cluster', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='org_list', to='main_events.Cluster')),
            ],
        ),
        migrations.CreateModel(
            name='HostType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Recurrence',
            fields=[
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='recurrence', serialize=False, to='main_events.Event')),
                ('freq', models.CharField(choices=[('None', 'None'), ('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')], default='None', help_text='How frequent is the recurrence?', max_length=50)),
                ('repeats', models.IntegerField(default=1, help_text='Every how many days/weeks/months?')),
                ('recur_days', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('6', 'Sunday'), ('0', 'Monday'), ('1', 'Tuesday'), ('2', 'Wednesday'), ('3', 'Thursday'), ('4', 'Friday'), ('5', 'Saturday')], help_text='If recurrence is weekly, on what days will the event occur on?', max_length=13, null=True)),
                ('end_recur_date', models.DateField(blank=True, help_text='Choose a date for when the recurrence will end', null=True)),
                ('end_recur_times', models.IntegerField(blank=True, help_text='Until how many occurrences for this event to end?', null=True)),
                ('datetimes', django.contrib.postgres.fields.ArrayField(base_field=models.DateField(), default=list, size=None)),
            ],
        ),
        migrations.AddField(
            model_name='eventhost',
            name='host_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='host_list', to='main_events.HostType'),
        ),
        migrations.AddField(
            model_name='event',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hosted_events', to='main_events.EventHost'),
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(related_name='event_list', to='main_events.Tag'),
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_events.Venue'),
        ),
    ]
