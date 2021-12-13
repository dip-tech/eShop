# Generated by Django 3.2.4 on 2021-11-20 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20210927_2333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('house_no', models.CharField(default='', max_length=100)),
                ('locality', models.CharField(default='', max_length=1000)),
                ('city', models.CharField(default='', max_length=100)),
                ('state', models.CharField(default='', max_length=100)),
                ('zipcode', models.CharField(default='', max_length=10)),
            ],
        ),
    ]