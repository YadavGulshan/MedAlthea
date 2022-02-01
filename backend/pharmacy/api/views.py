# pylint: disable=missing-module-docstring
# 
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/PharmaService > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from pharmacy.models import Medical, Medicine
from .serializers import MedicalSerializer, MedicineSerializer, RegisterSerializer

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

# Imports used in search functionality
from rest_framework import filters


# A method decorator to cache the view for 60 seconds
@method_decorator(cache_page(60), name='get')
# A method decorator to vary on the cookie
@method_decorator(vary_on_cookie, name='get')
# A method decorator to vary on the headers
@method_decorator(vary_on_headers, name='get')
# Allow only authenticated users to access this view
# @permission_classes([IsAuthenticated])
class MedicalView(APIView):
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


# @permission_classes([IsAuthenticated])
class MedicalViewList(APIView):
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

# @permission_classes([IsAuthenticated])
class MedicalSearch(generics.ListCreateAPIView):
    search_fields = ['name', 'address', 'phone']
    filter_backends = (filters.SearchFilter,)
    queryset = Medical.objects.all()
    serializer_class = MedicalSerializer

# @permission_classes([IsAuthenticated])
class MedicineView(APIView):
    def getObject(self, pk):
        try:
            return Medicine.objects.filter(pk=pk)
        except Medicine.DoesNotExist:
            return Http404

    def get(self, request, pk):
        medicine = self.getObject(pk)
        serializer = MedicineSerializer(medicine, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        medicine = self.getObject(pk)
        # Ensure that the user is the owner of the medicine
        if medicine[0].user.id != request.user.id:
            return Response("HTTP 403 Forbidden", status=403)
        serializer = MedicineSerializer(medicine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        medicine = self.getObject(pk)
        # Ensure that the user is the owner of the medicine
        if medicine[0].user.id != request.user.id:
            return Response("HTTP 403 Forbidden", status=403)
        medicine.delete()
        return Response("Deleted", status=200)

# @permission_classes([IsAuthenticated])
class MedicineViewList(APIView):
    def get(self, request, format=None):
        medicine = Medicine.objects.all()
        serializer = MedicineSerializer(medicine, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MedicineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# @permission_classes([IsAuthenticated])
class MedicineSearch(generics.ListCreateAPIView):
    search_fields = ['name', 'description']
    filter_backends = (filters.SearchFilter,)
    queryset= Medicine.objects.all()
    serializer_class = MedicineSerializer



