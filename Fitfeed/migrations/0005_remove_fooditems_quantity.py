# Generated by Django 4.2.6 on 2023-10-19 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Fitfeed', '0004_alter_consumeditems_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooditems',
            name='quantity',
        ),
    ]
