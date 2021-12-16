# Generated by Django 4.0 on 2021-12-16 08:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_employee_date_hire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='boss',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.boss'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_hire',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 12, 16, 14, 49, 48, 18539)),
        ),
    ]
