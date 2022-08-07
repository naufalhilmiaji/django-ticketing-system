# Generated by Django 4.1 on 2022-08-07 01:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trips', '0004_trip_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('total', models.FloatField()),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Pesanan dibuat'), (2, 'Diverifikasi'), (3, 'Dibayar'), (4, 'Selesai'), (5, 'Batal')], default=1)),
                ('is_verified', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ordered_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_by', to=settings.AUTH_USER_MODEL)),
                ('trip', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='trip', to='trips.trip')),
            ],
        ),
    ]
