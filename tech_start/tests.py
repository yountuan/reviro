import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Product, Establishment, Location

@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_location_viewset(api_client):
    user = User.objects.create(username='user', password='password')
    api_client.force_authenticate(user=user)

    Location.objects.create(address='address', city='city 1', country='country 1')
    Location.objects.create(address='address', city='city 2', country='country 2')

    response = api_client.get('/tech/locations/')
    assert response.status_code == 200
    assert len(response.json()['results']) == 2

    location_id = Location.objects.first().id
    response = api_client.get(f'/tech/locations/{location_id}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_establishment_viewset(api_client):
    user = User.objects.create(username='user', password='password')
    api_client.force_authenticate(user=user)
    
    location_1 = Location.objects.create(address = 'address', city='city 1', country='country 1')

    Establishment.objects.create(name='establishment 1', location=location_1)
    Establishment.objects.create(name='establishment 2', location=location_1)

    response = api_client.get('/tech/establishments/')
    assert response.status_code == 200
    assert len(response.json()['results']) == 2

    establishment_id = Establishment.objects.first().id
    response = api_client.get(f'/tech/establishments/{establishment_id}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_product_viewset(api_client):
    user = User.objects.create(username='user', password='password')
    api_client.force_authenticate(user=user)
    location_1 = Location.objects.create(address = 'address', city='city 1', country='country 1')
    establishment_1 = Establishment.objects.create(name='establishment', location=location_1)

    Product.objects.create(name='product 1', price=10, quantity=5, establishment=establishment_1)
    Product.objects.create(name='product 2', price=20, quantity=8, establishment=establishment_1)

    response = api_client.get('/tech/products/')
    assert response.status_code == 200
    assert len(response.json()['results']) == 2

    product_id = Product.objects.first().id
    response = api_client.get(f'/tech/products/{product_id}/')
    assert response.status_code == 200