# Generated by Django 4.2.3 on 2023-08-07 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_openness_max_company_alter_openness_max_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='count_person',
            field=models.IntegerField(default=1, verbose_name='人数'),
            preserve_default=False,
        ),
    ]
