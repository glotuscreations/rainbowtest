# Generated by Django 2.1.1 on 2018-10-02 06:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_auto_20181002_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 2, 9, 54, 45, 188429), null=True),
        ),
    ]
