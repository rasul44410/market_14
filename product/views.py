from .serializers import CategorySerializers, ProductSerializers
from .models import Product, Category
from rest_framework.viewsets import ModelViewSet


# Create your views here.

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
