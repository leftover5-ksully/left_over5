# Generated by Django 2.1.1 on 2018-10-30 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20181030_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favoriteItems',
            field=models.ManyToManyField(to='shop.Item'),
        ),
    ]
