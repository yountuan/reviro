from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(title='Products',
                 default_version='v1',
                 description='The products api documentation',
                 license=openapi.License(name='BSD license'),
                 ),
    public=True,
    permission_classes=[permissions.AllowAny,],

)
