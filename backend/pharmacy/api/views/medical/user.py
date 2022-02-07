# pylint: disable=missing-module-docstring
#
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/pharmaService > project,
# and is released under the "BSD 3-Clause License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from pharmacy.api.serializers import MedicalSerializer
from pharmacy.models import Medical


@permission_classes([IsAuthenticated])
class MyMedical(generics.ListCreateAPIView):
    serializer_class = MedicalSerializer

    def get(self, request):
        medical = Medical.objects.filter(user=request.user)
        serializer = MedicalSerializer(medical, many=True)
        return Response(serializer.data)
