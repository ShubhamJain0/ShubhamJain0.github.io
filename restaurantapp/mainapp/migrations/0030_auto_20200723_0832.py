# Generated by Django 2.2.2 on 2020-07-23 08:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0029_auto_20200723_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingtable',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
