# Generated by Django 2.1.1 on 2018-10-04 11:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_auto_20181003_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 4, 14, 40, 59, 462900), null=True),
        ),
    ]
