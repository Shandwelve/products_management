from django.db import models

from auditlog.registry import auditlog


class ProductCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name_plural = "Product categories"


class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=20)
    description = models.TextField(null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return str(self.name)


class ProductPrice(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="prices"
    )
    value = models.DecimalField(max_digits=6, decimal_places=2)
    date_from = models.DateField(null=True, blank=True)
    date_to = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.value)


auditlog.register(ProductPrice)
