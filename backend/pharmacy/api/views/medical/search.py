# pylint: disable=missing-module-docstring
#
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/pharmaService > project,
# and is released under the "BSD 3-Clause License Agreement".
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

# Decorators
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import  vary_on_headers

# A method decorator to cache the view for 2 hours
@method_decorator(cache_page(60*60*2), name="get")
# A method decorator to vary on the headers
@method_decorator(vary_on_headers("Authorization"), name="get")
@permission_classes([IsAuthenticated])
class MedicalSearch(generics.ListCreateAPIView):
    search_fields = ["name", "address", "phone"]
    filter_backends = (filters.SearchFilter,)
    queryset = Medical.objects.all()
    serializer_class = MedicalSerializer
