# Generated by Django 3.2.4 on 2021-10-04 16:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_eshopproducts_product_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eshopproducts',
            name='PRODUCT_DESC',
            field=ckeditor.fields.RichTextField(blank=True, default='', null=True),
        ),
    ]
