# Generated by Django 2.2.2 on 2020-06-04 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20200604_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(null=True, upload_to='media'),
        ),
    ]
