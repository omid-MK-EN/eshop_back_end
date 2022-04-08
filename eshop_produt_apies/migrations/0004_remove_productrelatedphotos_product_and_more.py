# Generated by Django 4.0.3 on 2022-04-08 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_produt_apies', '0003_productrelatedphotos_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productrelatedphotos',
            name='product',
        ),
        migrations.AddField(
            model_name='eshopproduct',
            name='product_photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_related', to='eshop_produt_apies.productrelatedphotos'),
        ),
    ]
