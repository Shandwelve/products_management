from rest_framework import routers

from products.views import ProductViewSet, ProductCategoryViewSet, ProductPriceViewSet

router = routers.DefaultRouter()
router.register(r"products", ProductViewSet, basename="products")
router.register(
    r"product_categories", ProductCategoryViewSet, basename="product_categories"
)
router.register(r"product_prices", ProductPriceViewSet, basename="product_prices")

urlpatterns = router.urls
