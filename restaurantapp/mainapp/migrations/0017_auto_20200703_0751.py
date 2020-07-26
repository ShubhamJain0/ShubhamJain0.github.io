# Generated by Django 2.2.2 on 2020-07-03 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_auto_20200703_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingtable',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bookingtable',
            name='persons',
            field=models.IntegerField(default=1, max_length=8),
        ),
        migrations.AlterField(
            model_name='bookingtable',
            name='phone',
            field=models.IntegerField(max_length=10),
        ),
    ]
