# Generated by Django 3.2.4 on 2021-09-16 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_buyer_userbuyer'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyerModel',
            fields=[
                ('buyer_id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('address', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='UserBuyer',
        ),
    ]