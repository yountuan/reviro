from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import ProductSerializer, EstablishmentSerializer, LocationSerializer
from .models import Product, Establishment, Location


class AllPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 50


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['price', 'quantity', 'name', 'establishment']
    search_fields = ['price', 'quantity', 'name', 'establishment']
    ordering_fields = ['id', 'name', 'price', 'quantity', 'establishment']
    ordering = ['id']
    pagination_class = AllPagination


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['country', 'city', 'opening_hours', 'closing_hours']
    search_fields = ['country', 'city', 'opening_hours', 'closing_hours']
    ordering_fields = ['id', 'opening_hours','closing_hours', 'city', 'country']
    ordering = ['id']
    pagination_class = AllPagination


class EstablishmentViewSet(viewsets.ModelViewSet):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['location', 'name']
    search_fields = ['location', 'name']
    ordering_fields = ['id', 'name', 'location',]
    ordering = ['id']
    pagination_class = AllPagination


    
