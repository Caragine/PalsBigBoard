# Generated by Django 4.1 on 2023-08-10 19:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 10, 19, 44, 40, 380068, tzinfo=datetime.timezone.utc)),
        ),
    ]
