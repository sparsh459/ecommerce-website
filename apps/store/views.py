from django.utils.translation import gettext_lazy
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from url_filter.integrations.drf import DjangoFilterBackend

from apps.store.models import Product
from apps.store.serializers.product_serializers import ProductSerializer, ProductDetailSerialier

class ProductViewset(ModelViewSet):
    """
    Viewset for Product
    """
    serializer_class = ProductDetailSerialier
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action in ("list",):
            return ProductSerializer
        return ProductDetailSerialier

    filter_fields = (
        "category",
        "price",
        "in_stock",
        "is_active",
    )
    ordering_fields = (
        "price",
        "created",
        "updated",
    )
    ordering = ("-created")
    search_fields = (
        "category",
        "title",
        "author",
    )

    # def perform_create(self, serializer):
    #     serializer.save(created_by=self.request.user)

    # def perform_update(self, serializer):
    #     serializer.save(updated_by=self.request.user)

