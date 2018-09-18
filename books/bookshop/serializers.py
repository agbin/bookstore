from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    #name = serializers.SlugRelatedField(slug_field='name', queryset=Product.objects.all())
    #author = serializers.SlugRelatedField(slug_field='name', queryset=Product.objects.all())
    categories = serializers.SlugRelatedField(many=True, read_only=True, slug_field='category_name')

    class Meta:
        model = Product
        fields = ('name', 'author', 'description', 'price', 'vat', 'stock', 'categories', 'book_logo')