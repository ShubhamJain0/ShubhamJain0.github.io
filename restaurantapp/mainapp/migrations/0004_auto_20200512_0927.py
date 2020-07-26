# Generated by Django 2.2.2 on 2020-05-12 09:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20200508_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='ordereddate',
            field=models.DateTimeField(default=datetime.date(2020, 5, 12)),
        ),
        migrations.AlterField(
            model_name='yourorder',
            name='ordereddate',
            field=models.DateTimeField(default=datetime.date(2020, 5, 12)),
        ),
        migrations.CreateModel(
            name='search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=200)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
