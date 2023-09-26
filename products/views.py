from __future__ import annotations

from datetime import date

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from products.models import Product, ProductCategory, ProductPrice
from products.serializers import (
    ProductSerializer,
    ProductCategorySerializer,
    ProductPriceSerializer,
)
from products.services import get_price_average_in_interval


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductPriceViewSet(viewsets.ModelViewSet):
    queryset = ProductPrice.objects.all()
    serializer_class = ProductPriceSerializer

    @action(detail=True, methods=["get"], name="price_average")
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "date_from",
                openapi.IN_QUERY,
                description="Date in format %s. Example: 1695712647",
                type=openapi.TYPE_STRING,
                required=True,
            ),
            openapi.Parameter(
                "date_to",
                openapi.IN_QUERY,
                description="Date in format %s. Example: 1695712647",
                type=openapi.TYPE_STRING,
                required=True,
            ),
        ]
    )
    def price_average(self, request: Request, pk: int | None = None) -> Response:
        product = Product.objects.get(pk=pk)
        date_from = date.fromtimestamp(int(request.query_params["date_from"]))
        date_to = date.fromtimestamp(int(request.query_params["date_to"]))
        price_average = get_price_average_in_interval(product, date_from, date_to)

        return Response("{:.2f}".format(price_average))
