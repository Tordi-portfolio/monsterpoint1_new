# Generated by Django 5.1.5 on 2025-07-20 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gram',
            field=models.CharField(default=2025, max_length=10),
            preserve_default=False,
        ),
    ]
