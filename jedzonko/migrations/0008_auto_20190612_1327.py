# Generated by Django 2.1.2 on 2019-06-12 11:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0007_auto_20190612_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jedzonkorecipe',
            name='created',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
