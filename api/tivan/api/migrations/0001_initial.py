# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('description', models.TextField(default=b'')),
                ('stream_url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CapturePicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.TextField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CaptureVideo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('stop_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField()),
                ('stop_time', models.DateTimeField(null=True)),
                ('changed_pixels', models.IntegerField()),
                ('noise_level', models.IntegerField()),
                ('motion_area_width', models.IntegerField()),
                ('motion_area_height', models.IntegerField()),
                ('motion_center_x', models.IntegerField()),
                ('motion_center_y', models.IntegerField()),
                ('camera', models.ForeignKey(to='api.Camera')),
            ],
        ),
        migrations.AddField(
            model_name='capturevideo',
            name='event',
            field=models.ForeignKey(to='api.Event'),
        ),
        migrations.AddField(
            model_name='capturepicture',
            name='event',
            field=models.ForeignKey(to='api.Event'),
        ),
        migrations.AlterUniqueTogether(
            name='event',
            unique_together=set([('camera', 'start_time')]),
        ),
    ]
