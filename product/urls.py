from rest_framework.routers import SimpleRouter
# from django.urls import path, include
from .views import CategoryViewSet, ProductViewSet

router = SimpleRouter()
router.register('categories', CategoryViewSet)
router.register('product', ProductViewSet)


urlpatterns = [
]
