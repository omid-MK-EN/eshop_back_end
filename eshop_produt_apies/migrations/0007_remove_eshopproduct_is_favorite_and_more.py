# Generated by Django 4.0.3 on 2022-04-08 06:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eshop_produt_apies', '0006_remove_eshopproduct_product_photo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eshopproduct',
            name='is_favorite',
        ),
        migrations.AddField(
            model_name='eshopproduct',
            name='favorite',
            field=models.ManyToManyField(blank=True, null=True, related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]
