# Generated by Django 3.2.4 on 2021-12-11 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_eshopproducts_sold_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='eshopproducts',
            name='IS_ACTIVE',
            field=models.CharField(default='1', max_length=10),
        ),
    ]
