# Generated by Django 3.2.3 on 2021-05-26 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.CharField(max_length=50, verbose_name='Stock')),
                ('close_price', models.FloatField(verbose_name='Close Price')),
                ('date', models.CharField(max_length=50, verbose_name='Date')),
            ],
        ),
    ]
