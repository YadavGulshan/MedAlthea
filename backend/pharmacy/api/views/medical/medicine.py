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
from ...serializers import MedicalSerializer, MedicineSerializer

from rest_framework import generics
from rest_framework import status


@permission_classes([IsAuthenticated])
class MedicineViewList(generics.CreateAPIView):
    """This class will display or help medical owner view or update the medicines."""

    def get(self, request):
        medicine = Medicine.objects.filter(user=request.user)
        serializer = MedicalSerializer(medicine, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MedicineViewByID(generics.CreateAPIView):
    """ "This class will display only the medicine owned by specific medical shop."""

    def get(self, request, pk):
        # First check if the medical shop exists
        try:
            medical = Medical.objects.get(pk=pk)
        except Medical.DoesNotExist:
            raise Http404

        # Check if that medical shop is owned by the user
        if medical.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        # medical = Medical.objects.filter(user=request.user)
        try:
            medicine = Medicine.objects.get(pk=pk)
        except Medicine.DoesNotExist:
            raise Http404
        serializer = MedicineSerializer(medicine)
        return Response(serializer.data, status=status.HTTP_200_OK)
