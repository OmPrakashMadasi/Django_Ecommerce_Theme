# Generated by Django 4.2.6 on 2024-02-08 08:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_remove_payment_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]