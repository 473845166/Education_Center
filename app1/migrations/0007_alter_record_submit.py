# Generated by Django 4.2.3 on 2023-08-07 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_record_submit_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='submit',
            field=models.DateTimeField(auto_created=True, verbose_name='创建时间'),
        ),
    ]