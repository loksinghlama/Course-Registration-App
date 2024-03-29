# Generated by Django 2.2.2 on 2019-08-06 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoAuthentication', '0022_auto_20190806_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statustable',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stud_session', to='djangoAuthentication.StudentManagement'),
        ),
        migrations.AlterField(
            model_name='statustable',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stud_status', to='djangoAuthentication.GradeManagement'),
        ),
    ]
