from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, LocationViewSet, EstablishmentViewSet
from .swagger import *

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'establishments', EstablishmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
