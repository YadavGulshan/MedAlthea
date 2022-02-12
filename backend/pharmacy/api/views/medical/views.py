# pylint: disable=missing-module-docstring
#
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/pharmaService > project,
# and is released under the "BSD 3-Clause License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from pharmacy.models import Medical
from ...serializers import MedicalSerializer


# Imports for caching
from rest_framework.views import APIView
from rest_framework import status

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers


# A method decorator to cache the view for 2 hours
@method_decorator(cache_page(60 * 60 * 2), name="get")
# A method decorator to vary on the headers
@method_decorator(vary_on_headers("Authorization"), name="get")
# Allow only authenticated users to access this view
@permission_classes([IsAuthenticated])
class MedicalView(APIView):
    def getObject(self, pk):
        try:
            return Medical.objects.filter(pk=pk)
        except Medical.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        medical = self.getObject(pk)
        serializer = MedicalSerializer(medical, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        medical = self.getObject(pk)
        # Ensure that the user is the owner of the medical
        if medical[0].user.id != request.user.id:
            return Response("HTTP 403 Forbidden", status=status.HTTP_403_FORBIDDEN)
        serializer = MedicalSerializer(medical, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        medical = self.getObject(pk)
        # Ensure that the user is the owner of the medical
        if medical[0].user.id != request.user.id:
            return Response("HTTP 403 Forbidden", status=status.HTTP_403_FORBIDDEN)
        medical.delete()
        return Response("Deleted", status=status.HTTP_202_ACCEPTED)
