# Generated by Django 2.1.2 on 2019-06-13 18:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0012_auto_20190613_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jedzonkorecipe',
            name='created',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='jedzonkorecipe',
            name='updated',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
