# Generated by Django 2.1.5 on 2019-02-18 18:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190204_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_news',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 18, 20, 2, 33, 673958)),
        ),
    ]
