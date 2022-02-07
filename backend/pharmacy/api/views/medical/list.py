# pylint: disable=missing-module-docstring
# 
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/pharmaService > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from pharmacy.api.views.userActions.token import serializer

from pharmacy.models import Medical
from ...serializers import MedicalSerializer

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status

@permission_classes([IsAuthenticated])
class MedicalViewList(generics.CreateAPIView):
    serializer_class = MedicalSerializer
    def get(self, request):
        medical = Medical.objects.all()
        serializer = MedicalSerializer(medical, many=True)
        return Response(serializer.data)

    
    def post(self, request):
        serializer = MedicalSerializer(data=request.data)
        # Make serializer mutable
        serializer.initial_data = serializer.initial_data.copy()
        # Set the user to the logged in user
        serializer.initial_data['user'] = request.user.id
        if serializer.is_valid():
            if request.user.is_staff:
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)