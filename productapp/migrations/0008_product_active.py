# Generated by Django 3.0.3 on 2020-05-20 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0007_auto_20200519_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
