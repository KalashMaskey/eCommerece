# Generated by Django 3.0.3 on 2020-05-21 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0014_auto_20200521_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
