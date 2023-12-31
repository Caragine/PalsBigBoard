# Generated by Django 4.1 on 2023-09-01 03:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bets', '0006_bet_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='loser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='UpdateBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winamount', models.PositiveIntegerField()),
                ('loseamount', models.PositiveIntegerField()),
                ('loser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='betloser', to=settings.AUTH_USER_MODEL)),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='betwinner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
