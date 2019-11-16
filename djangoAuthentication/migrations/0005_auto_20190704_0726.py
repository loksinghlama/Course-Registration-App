# Generated by Django 2.2.2 on 2019-07-04 01:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoAuthentication', '0004_auto_20190704_0717'),
    ]

    operations = [
        migrations.CreateModel(
            name='Firebase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='studentmanagement',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 4, 7, 26, 26, 716639)),
        ),
        migrations.AlterField(
            model_name='studentmanagement',
            name='enrolled_year',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 4, 7, 26, 26, 716639)),
        ),
    ]