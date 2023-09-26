from decimal import Decimal
from datetime import date

from django.db.models import Q

from products.models import Product, ProductPrice


def get_price_average_in_interval(
    product: Product, date_from: date, date_to: date
) -> Decimal:
    records = ProductPrice.objects.filter(
        Q(date_from__isnull=True) | Q(date_from__lte=date_to),
        Q(date_to__isnull=True) | Q(date_to__gte=date_from),
        product=product,
    )

    days = 0
    price = Decimal(0)
    minimal_date = date(1, 1, 1)
    maximal_date = date(9999, 12, 31)

    for record in records:
        date_start = record.date_from
        if date_start is None:
            date_start = minimal_date

        if date_from > date_start:
            date_start = date_from

        date_end = record.date_to
        if date_end is None:
            date_end = maximal_date

        if date_to < date_end:
            date_end = date_to

        delta = date_end - date_start
        price += record.value * (delta.days + 1)
        days += delta.days + 1

    if days == 0:
        return Decimal(0)

    return price / days
