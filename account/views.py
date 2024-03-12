from django.shortcuts import render
from rest_framework.views import APIView

from account.tasks import send_activation_code_celery
from .serializers import RegisterSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status


User = get_user_model()


class RegisterView(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer())
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        activation_code = user.activation_code
        send_activation_code_celery.delay(user.email, activation_code)

        # Отправка активационного кода на email
        # send_activation_code_celery.delay(user.email, activation_code)

        return Response({'message': 'Successfully registered',
                         'activation_code': activation_code}, status=status.HTTP_201_CREATED)
    

class ActivationView(APIView):
    def get(self, request, email, activation_code):
        user = User.objects.filter(email=email, activation_code=activation_code).first()
        if not user:
            return Response('User does not exist', status=400)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response('Successfully activated', status=200)
    

class DeleteAccountView(APIView):
    def delete(self, request, email):
        try:
            user = User.objects.get(email=email)
            user.delete()
            return Response('Account successfully deleted', status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response('User does not exist', status=status.HTTP_404_NOT_FOUND)