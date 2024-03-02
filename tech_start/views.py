from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import ProductSerializer, EstablishmentSerializer, LocationSerializer
from .models import Product, Establishment, Location


class AllPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 50

    

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['price', 'quantity', 'name']
    search_fields = ['price', 'quantity', 'name']
    ordering_fields = ['name', 'price', 'quantity']
    ordering = ['quantity']
    pagination_class = AllPagination



class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['country', 'city', 'opening_hours']
    search_fields = ['country', 'city', 'opening_hours']
    ordering_fields = ['opening_hours', 'city', 'country']
    ordering = ['opening_hours']
    pagination_class = AllPagination



class EstablishmentViewSet(viewsets.ModelViewSet):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['location', 'name']
    search_fields = ['location', 'name']
    pagination_class = AllPagination


    
