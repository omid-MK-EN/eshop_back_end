# Generated by Django 4.0.3 on 2022-04-10 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_produt_apies', '0008_alter_eshopproduct_brand_alter_eshopproduct_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eshopproduct',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='eshop_produt_apies.eshopproductcategory'),
        ),
    ]