# Generated by Django 4.0.3 on 2022-04-06 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_contact_us_apies', '0002_eshopforwardcontactusmessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eshopcontactus',
            name='read_time',
        ),
    ]
