# Generated by Django 3.1.2 on 2020-10-05 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('is_customizable', models.BooleanField()),
                ('relative_url', models.CharField(blank=True, max_length=500)),
                ('price', models.CharField(blank=True, max_length=500)),
                ('product_main_image', models.CharField(blank=True, max_length=500)),
                ('delivery', models.CharField(blank=True, max_length=500)),
                ('discount_type', models.CharField(blank=True, max_length=500, null=True)),
                ('is_exclusive', models.BooleanField(blank=True)),
                ('prices', models.JSONField(blank=True)),
                ('id', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('currency', models.CharField(blank=True, max_length=500)),
                ('attribute_english', models.JSONField(blank=True)),
                ('name', models.CharField(blank=True, max_length=500)),
                ('discount_percentage', models.PositiveSmallIntegerField(blank=True)),
                ('url', models.CharField(blank=True, max_length=500)),
                ('product_labels', models.JSONField(blank=True)),
                ('online', models.BooleanField(blank=True)),
                ('price_old', models.CharField(blank=True, max_length=500)),
                ('min_max_prices', models.JSONField(blank=True)),
                ('attributes', models.JSONField(blank=True)),
                ('image', models.CharField(blank=True, max_length=500)),
                ('stock', models.JSONField(blank=True)),
            ],
        ),
    ]
