# Generated by Django 2.2.2 on 2020-07-06 08:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0024_auto_20200706_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingtable',
            name='time',
            field=models.TimeField(choices=[('', 'Time'), ('10 A.M', '10 A.M'), ('10:30 A.M', '10:30 A.M'), ('11 A.M', '11 A.M'), ('11:30 A.M', '11:30 A.M'), ('12 P.M', '12 P.M'), ('12:30 P.M', '12:30 P.M'), ('1 P.M', '1 P.M'), ('1:30 P.M', '1:30 P.M'), ('2 P.M', '2 P.M'), ('2:30 P.M', '2:30 P.M'), ('3 P.M', '3 P.M'), ('3:30 P.M', '3:30 P.M'), ('4 P.M', '4 P.M'), ('4:30 P.M', '4:30 P.M'), ('5 P.M', '5 P.M'), ('5:30 P.M', '5:30 P.M'), ('6 P.M', '6 P.M'), ('6:30 P.M', '6:30 P.M'), ('7 P.M', '7 P.M'), ('7:30 P.M', '7:30 P.M'), ('8 P.M', '8 P.M'), ('8:30 P.M', '8:30 P.M'), ('9 P.M', '9 P.M'), ('9:30 P.M', '9:30 P.M'), ('10 P.M', '10 P.M')], default=django.utils.timezone.now),
        ),
    ]
