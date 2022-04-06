# Generated by Django 4.0.3 on 2022-04-06 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_contact_us_apies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EshopForwardContactUsMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_forward', models.CharField(blank=True, max_length=50, null=True)),
                ('forward_message', models.TextField()),
                ('forward_time', models.DateTimeField(auto_now=True)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forward_message', to='eshop_contact_us_apies.eshopcontactus')),
            ],
        ),
    ]
