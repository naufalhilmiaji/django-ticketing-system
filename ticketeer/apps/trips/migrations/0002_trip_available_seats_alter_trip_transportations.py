# Generated by Django 4.1 on 2022-08-06 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportations', '0002_alter_transportation_type'),
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='available_seats',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='transportations',
            field=models.ManyToManyField(related_name='trips', to='transportations.transportation'),
        ),
    ]