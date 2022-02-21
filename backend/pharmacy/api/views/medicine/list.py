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

from pharmacy.models import Medical, Medicine
from ...serializers import MedicineSerializer

# Imports for caching
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status


@permission_classes([IsAuthenticated])
class MedicineViewList(generics.ListCreateAPIView):
    serializer_class = MedicineSerializer

    def getObject(self, pk):
        try:
            return Medical.objects.filter(pk=pk)
        except Medical.DoesNotExist:
            return Http404

    def get(self, request, format=None):
        medicine = Medicine.objects.all()
        serializer = MedicineSerializer(medicine, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Ensure that the user is the owner of the medical shop
        medical = self.getObject(request.data['medicalId'])

        # If the user is not the owner of the medical shop, return 403
        if medical[0].user.id != request.user.id:
            return Response("HTTP 403 Forbidden", status=status.HTTP_403_FORBIDDEN)
        
        
        serializer = MedicineSerializer(data=request.data)
        # Make serializer mutable
        serializer.initial_data = serializer.initial_data.copy()
        # Set the user to the logged in user
        serializer.initial_data["user"] = request.user.id

        if serializer.is_valid():
            # Check if the user is staff
            if request.user.is_staff:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(
                serializer.errors, status=status.HTTP_405_METHOD_NOT_ALLOWED
            )
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
