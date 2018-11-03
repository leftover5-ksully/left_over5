# Generated by Django 2.1.1 on 2018-10-29 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20181029_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storename', models.CharField(default='DEFAULT', max_length=100)),
                ('stock', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.List')),
            ],
        ),
    ]
