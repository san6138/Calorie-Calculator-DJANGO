# Generated by Django 4.2.6 on 2023-10-18 22:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Fitfeed', '0003_alter_consumeditems_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumeditems',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]