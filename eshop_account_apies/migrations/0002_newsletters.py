# Generated by Django 4.0.3 on 2022-04-07 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_account_apies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
