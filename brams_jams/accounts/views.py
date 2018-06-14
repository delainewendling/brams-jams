# Create your views here.
import jwt, json
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User


class Login(APIView):

    def post(self, request, *args, **kwargs):
        try:
            email = request.data['email']
            password = request.data['password']
        except KeyError:
            return Response({'Error': "Please provide email/password"}, status="400")

        try:
            user = User.objects.get(email=email, password=password)
        except User.DoesNotExist:
            return Response({'Error': "Invalid email/password"}, status="400")

        return try_to_log_user_in(user)


class SignUp(APIView):

    def post(self, request, *args, **kwargs):

        try:
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            email = request.data['email']
            password = request.data['password']
        except KeyError:
            return Response({'Error': "Please provide all required fields"}, status="400")

        existing_user = User.objects.filter(email=email, password=password)

        if existing_user:
            return Response({'Error': "A user with this email already exists, please login"}, status="400")

        try:
            user = User.objects.create(
                            first_name=first_name,
                            last_name=last_name,
                            email=email,
                            password=password
                        )
        except Exception as e:
            return Response({'Error': "There was an error creating this user"}, status="400")

        return try_to_log_user_in(user)


def try_to_log_user_in(user):
    if user:
        payload = {
            'id': user.id,
            'email': user.email,
        }
        jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}

        return Response(
            json.dumps(jwt_token),
            status=200,
            content_type="application/json"
        )
    else:
        return Response(
            json.dumps({'Error': "Invalid credentials"}),
            status=400,
            content_type="application/json"
        )