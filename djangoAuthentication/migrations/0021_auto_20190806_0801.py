# Generated by Django 2.2.2 on 2019-08-06 02:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoAuthentication', '0020_remove_coursemanagement_prerequisite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deadline',
            name='end_date',
            field=models.DateField(default=datetime.date(2019, 8, 6)),
        ),
        migrations.AlterField(
            model_name='deadline',
            name='start_date',
            field=models.DateField(default=datetime.date(2019, 8, 6)),
        ),
        migrations.AlterField(
            model_name='studentmanagement',
            name='date_created',
            field=models.DateField(default=datetime.date(2019, 8, 6)),
        ),
        migrations.AlterField(
            model_name='studentmanagement',
            name='enrolled_year',
            field=models.DateField(default=datetime.date(2019, 8, 6)),
        ),
        migrations.CreateModel(
            name='StatusTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoAuthentication.CourseManagement')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='session', to='djangoAuthentication.StudentManagement')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoAuthentication.GradeManagement')),
                ('university_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stud_id', to='djangoAuthentication.StudentManagement')),
            ],
        ),
    ]