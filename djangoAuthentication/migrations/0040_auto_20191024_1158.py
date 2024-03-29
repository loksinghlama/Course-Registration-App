# Generated by Django 2.2 on 2019-10-24 06:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoAuthentication', '0039_auto_20191022_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessionnametable',
            name='date_created',
            field=models.DateField(default=datetime.date(2019, 10, 24)),
        ),
        migrations.AlterField(
            model_name='sessionnametable',
            name='end_date',
            field=models.DateField(default=datetime.date(2019, 10, 24)),
        ),
        migrations.AlterField(
            model_name='sessionnametable',
            name='start_date',
            field=models.DateField(default=datetime.date(2019, 10, 24)),
        ),
        migrations.AlterField(
            model_name='studentmanagement',
            name='date_created',
            field=models.DateField(default=datetime.date(2019, 10, 24)),
        ),
        migrations.AlterField(
            model_name='studentmanagement',
            name='enrolled_year',
            field=models.DateField(default=datetime.date(2019, 10, 24)),
        ),
    ]
