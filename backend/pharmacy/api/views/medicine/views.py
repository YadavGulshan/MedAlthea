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

from pharmacy.models import Medicine
from ...serializers import MedicineSerializer
from rest_framework import status

# Imports for caching
from rest_framework import generics


@permission_classes([IsAuthenticated])
class MedicineView(generics.RetrieveUpdateDestroyAPIView):
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
        # Print the medicine details
        print(medicine[0].name)
        # Ensure that the user is the owner of the medicine
        if medicine[0].user.id != request.user.id:
            return Response("HTTP 403 Forbidden", status=status.HTTP_403_FORBIDDEN)
        serializer = MedicineSerializer(medicine[0], data=request.data)

        # Update the user to the logged in user
        serializer.initial_data["user"] = request.user.id

        # Make serializer mutable
        # serializer.initial_data = serializer.initial_data.copy()
        # Set the user to the logged in user
        # serializer.initial_data["user"] = request.user.id
        if serializer.is_valid():
            # Print all the data
            # print(serializer.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        medicine = self.getObject(pk)
        # Ensure that the user is the owner of the medicine
        if medicine[0].user.id != request.user.id:
            return Response("HTTP 403 Forbidden", status=status.HTTP_403_FORBIDDEN)
        medicine.delete()
        return Response("Deleted", status=status.HTTP_202_ACCEPTED)
