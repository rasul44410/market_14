from rest_framework import serializers
from product.models import Category, Product


class ChildCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'parent', 'name'


class CategorySerializers(serializers.ModelSerializer):
    child_category = ChildCategorySerializers(source='category_set', many=True, read_only=True)

    class Meta:
        model = Category
        fields = 'parent', 'name', 'child_category',


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        name = Product
        fields = '__all__'


