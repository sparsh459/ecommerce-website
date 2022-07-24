from rest_framework import serializers
from apps.store.models import Product

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product View
    """
    
    class Meta:
        model = Product
        fields = "__all__"

class ProductDetailSerialier(serializers.ModelSerializer):
    """
    Detail Serializer for Product View
    """
    category = serializers.SerializerMethodField(read_only=True)

    def get_category(self, obj):
        return {
            "id" : obj.category.id,
            "name": obj.category.name
        }

    class Meta:
        model = Product
        fields = "__all__"