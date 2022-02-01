# pylint: disable=missing-module-docstring
# 
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/pharmaService > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from pharmacy.models import Medical
from ...serializers import MedicalSerializer

# Imports for registering a new user
from rest_framework import generics

# Imports used in search functionality
from rest_framework import filters



@permission_classes([IsAuthenticated])
class MedicalSearch(generics.ListCreateAPIView):
    search_fields = ['name', 'address', 'phone']
    filter_backends = (filters.SearchFilter,)
    queryset = Medical.objects.all()
    serializer_class = MedicalSerializer

