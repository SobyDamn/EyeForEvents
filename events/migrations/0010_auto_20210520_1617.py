# Generated by Django 3.2.3 on 2021-05-20 10:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20210520_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 20, 10, 47, 6, 879290, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_image',
            field=models.ImageField(blank=True, null=True, upload_to='events/f5c1094c-d214-4272-92bd-11e3581d84f6'),
        ),
        migrations.AlterField(
            model_name='event',
            name='last_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 20, 10, 47, 6, 879290, tzinfo=utc)),
        ),
    ]
