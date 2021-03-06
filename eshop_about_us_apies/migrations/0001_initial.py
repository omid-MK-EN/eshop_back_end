# Generated by Django 4.0.3 on 2022-04-05 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.CharField(max_length=30)),
                ('fax', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=30)),
                ('compane_descriptions', models.TextField()),
                ('adress', models.TextField()),
                ('logo', models.ImageField(upload_to='eshop_about_us_log/')),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
