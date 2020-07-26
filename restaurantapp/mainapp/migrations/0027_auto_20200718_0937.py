# Generated by Django 2.2.2 on 2020-07-18 09:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0026_auto_20200706_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingtable',
            name='date',
            field=models.DateField(default=datetime.date(2020, 7, 18)),
        ),
        migrations.AlterField(
            model_name='cartitems',
            name='ordereddate',
            field=models.DateTimeField(default=datetime.date(2020, 7, 18)),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordereddate',
            field=models.DateTimeField(default=datetime.date(2020, 7, 18)),
        ),
        migrations.AlterField(
            model_name='orderfood',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='yourorder',
            name='ordereddate',
            field=models.DateTimeField(default=datetime.date(2020, 7, 18)),
        ),
    ]