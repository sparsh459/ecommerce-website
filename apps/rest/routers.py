from rest_framework import routers
from apps.store.views import ProductViewset

router = routers.DefaultRouter()

router.register(r"products", ProductViewset, basename="products")