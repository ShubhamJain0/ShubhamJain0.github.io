# Generated by Django 2.2.2 on 2020-07-03 07:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_auto_20200703_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingtable',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
