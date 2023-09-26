from typing import Any

from rest_framework import serializers

from products.models import Product, ProductPrice, ProductCategory


class ProductCategorySerializer(serializers.ModelSerializer[ProductCategory]):
    id = serializers.ReadOnlyField()

    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductPriceSerializer(serializers.ModelSerializer[ProductPrice]):
    id = serializers.ReadOnlyField()
    date_from = serializers.DateField(format="%s")
    date_to = serializers.DateField(format="%s")
    product = serializers.PrimaryKeyRelatedField(
        write_only=True, read_only=False, queryset=Product.objects.all()
    )

    class Meta:
        model = ProductPrice
        fields = ("id", "value", "date_from", "date_to", "product")


class ProductSerializer(serializers.ModelSerializer[Product]):
    id = serializers.ReadOnlyField()
    prices = ProductPriceSerializer(many=True, required=False)

    def create(self, validated_data: dict[str, Any]) -> Product:
        prices = []

        if "prices" in validated_data:
            prices = validated_data.pop("prices")

        product = super().create(validated_data)

        for price in prices:
            ProductPrice.objects.create(product=product, **price)

        return product

    def update(self, instance: Product, validated_data: dict[str, Any]) -> Product:
        if "prices" in validated_data:
            for price in validated_data.pop("prices"):
                ProductPrice.objects.get(uuid=price["id"]).update(**price)

        return super().update(instance, validated_data)

    class Meta:
        model = Product
        fields = ("id", "name", "sku", "description", "category", "prices")
