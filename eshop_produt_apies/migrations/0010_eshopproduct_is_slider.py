# Generated by Django 4.0.3 on 2022-04-10 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_produt_apies', '0009_alter_eshopproduct_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='eshopproduct',
            name='is_slider',
            field=models.BooleanField(default=False),
        ),
    ]
