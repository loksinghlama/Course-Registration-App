# Generated by Django 2.2 on 2019-07-08 02:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoAuthentication', '0012_remove_firebasedatabase_fori'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmanagement',
            name='date_created',
            field=models.DateField(default=datetime.date(2019, 7, 8)),
        ),
        migrations.AlterField(
            model_name='studentmanagement',
            name='enrolled_year',
            field=models.DateField(default=datetime.date(2019, 7, 8)),
        ),
    ]
