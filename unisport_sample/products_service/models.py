from django.db import models

class Product(models.Model):
    is_customizable = models.BooleanField()
    relative_url = models.CharField(max_length=500, blank=True)
    price = models.CharField(max_length=500, blank=True)
    product_main_image = models.CharField(max_length=500, blank=True)
    delivery = models.CharField(max_length=500, blank=True)
    discount_type = models.CharField(max_length=500, blank=True, null=True)
    is_exclusive = models.BooleanField(blank=True)
    prices = models.JSONField(blank=True)
    id = models.PositiveBigIntegerField(primary_key=True)
    currency = models.CharField(max_length=500, blank=True)
    attribute_english = models.JSONField(blank=True)
    name = models.CharField(max_length=500, blank=True)
    discount_percentage = models.PositiveSmallIntegerField(blank=True)
    url = models.CharField(max_length=500, blank=True)
    product_labels = models.JSONField(blank=True)
    online = models.BooleanField(blank=True)
    price_old = models.CharField(max_length=500, blank=True)
    min_max_prices = models.JSONField(blank=True)
    attributes = models.JSONField(blank=True)
    image = models.CharField(max_length=500, blank=True)
    stock = models.JSONField(blank=True)