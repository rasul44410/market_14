from rest_framework import serializers
from product.models import Category, Product


class ChildCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'parent', 'name'

class ChildProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializers(serializers.ModelSerializer):
    child_category = ChildCategorySerializers(source='category_set', many=True, read_only=True)
    product_obj = ChildProductSerializers(source='product_set', many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):
    category_obj = CategorySerializers(source='category', many=False, read_only=True)
    class Meta:
        model = Product
        fields = "id", "name", "full_name", "price", "descriptions", "category", "category_obj"


