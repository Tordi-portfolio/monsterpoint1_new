# Generated by Django 5.0 on 2025-07-12 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0005_alter_shipment_current_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='destination_country_state',
            field=models.CharField(default=2020, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shipment',
            name='destination_country_town',
            field=models.CharField(default=0.9995051954477981, max_length=100),
            preserve_default=False,
        ),
    ]
