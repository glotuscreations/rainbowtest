# Generated by Django 2.1.1 on 2018-10-03 19:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_userprofiles_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofiles',
            name='age',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(18)]),
        ),
    ]
