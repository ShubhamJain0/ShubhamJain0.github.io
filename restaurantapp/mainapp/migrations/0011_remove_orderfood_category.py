# Generated by Django 2.2.2 on 2020-06-09 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20200609_0933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderfood',
            name='category',
        ),
    ]