# Generated by Django 2.2.2 on 2020-07-19 07:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0027_auto_20200718_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingtable',
            name='date',
            field=models.DateField(default=datetime.date(2020, 7, 19)),
        ),
        migrations.AlterField(
            model_name='cartitems',
            name='ordereddate',
            field=models.DateTimeField(default=datetime.date(2020, 7, 19)),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordereddate',
            field=models.DateTimeField(default=datetime.date(2020, 7, 19)),
        ),
        migrations.AlterField(
            model_name='yourorder',
            name='ordereddate',
            field=models.DateTimeField(default=datetime.date(2020, 7, 19)),
        ),
        migrations.AlterField(
            model_name='yourorder',
            name='ordereditems',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
