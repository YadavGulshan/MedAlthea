from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from pharmacy.models import Medical
from .serializers import MedicalSerializer, RegisterSerializer

# For customizing user claims
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Imports for caching
from rest_framework.views import APIView

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers


# Imports for registering a new user
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['email'] = user.email

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# A method decorator to cache the view for 60 seconds
@method_decorator(cache_page(60), name='get')
# A method decorator to vary on the cookie
@method_decorator(vary_on_cookie, name='get')
# A method decorator to vary on the headers
# @method_decorator(vary_on_headers, name='get')
# Allow only authenticated users to access this view
@permission_classes([IsAuthenticated])
class Data(APIView):
    def getObject(self, pk):
        try:
            return Medical.objects.filter(pk=pk)
        except Medical.DoesNotExist:
            return Http404

    def get(self, request, pk):
        medical = self.getObject(pk)
        serializer = MedicalSerializer(medical, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        medical = self.getObject(pk)
        # Ensure that the user is the owner of the medical
        if medical[0].user.id != request.user.id:
            return Response("HTTP 403 Forbidden", status=403)
        serializer = MedicalSerializer(medical, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        medical = self.getObject(pk)
        # Ensure that the user is the owner of the medical
        if medical[0].user.id != request.user.id:
            return Response("HTTP 403 Forbidden", status=403)
        medical.delete()
        return Response("Deleted", status=200)


@permission_classes([IsAuthenticated])
class DataList(APIView):
    def get(self, request, format=None):
        medical = Medical.objects.all()
        serializer = MedicalSerializer(medical, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MedicalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@permission_classes([IsAuthenticated])
class UserData(APIView):
    def get(self, request, format=None):
        current_user = request.user
        user = {
            'id': current_user.id,
            'username': current_user.username,
            'email': current_user.email,
        }
        return Response(user, status=200)


class Register(generics.CreateAPIView):
    """
    CreateAPIView is a generic class-based view that allows you to handle POST requests.

    This class is used to register a new user.
    """

    queryset = User.objects.all()
    """
    Queryset is used to get all the users
    """

    permission_classes = (AllowAny,)
    """
    Allow only unauthenticated users to access this view
    """

    serializer_class = RegisterSerializer
    """
    Now registering the serializer we created in serializers.py
    """

