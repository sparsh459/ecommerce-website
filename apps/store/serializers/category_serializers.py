from apps.store.models import Category
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for category
    """
    class Meta:
        model = Category
        fields = "__all__"