# Generated by Django 3.1.5 on 2021-01-18 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0004_auto_20210118_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standard',
            name='objective',
            field=models.TextField(null=True),
        ),
    ]
