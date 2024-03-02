from django.test import TestCase

from django.contrib.auth.models import User
from django.test import TestCase
from .serializers import ProductSerializer
from .models import Product
import pytest
from django.urls import reverse




@pytest.mark.django_db
def test_user_create():
  User.objects.create_user('username', 'password')
  assert User.objects.count() == 1


@pytest.mark.django_db
def test_user_detail(client, django_user_model):
   user = django_user_model.objects.create(
       username='someone', password='password'
   )
   url = reverse('user-detail-view', kwargs={'pk': user.pk})
   response = client.get(url)
   assert response.status_code == 200
   assert 'someone' in response.content


# class SerializerTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='user', password='password')
#         self.product = Product.objects.create(name='Milk', description='Description', price=500, quantity='50')

#     def test_data(self):
#         data = ProductSerializer(self.product).data
#         expected_data = {
#             'id': self.product.id,
#             'name': 'Milk',
#             'description': 'Description',
#             'price': '500.00',
#             'quantity': 50,

#         }
#         self.assertEqual(expected_data, data)