# Generated by Django 4.1 on 2022-08-07 00:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('transportations', '0003_transportation_units'),
    ]

    operations = [
        migrations.AddField(
            model_name='transportation',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
