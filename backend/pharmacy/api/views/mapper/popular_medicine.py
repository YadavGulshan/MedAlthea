# pylint: disable=missing-module-docstring
#
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/pharmaService > project,
# and is released under the "BSD 3-Clause License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

from collections import Counter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from pharmacy.api.tools import tools

from pharmacy.models import Medical, Medicine, PopularMedicine

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers


# @method_decorator(cache_page(60 * 5), name="get")
@method_decorator(vary_on_headers("Authorization"), name="get")
@method_decorator(vary_on_headers("Accept"), name="get")
# @permission_classes([IsAuthenticated])
class PopularMedicineSearch(APIView):
    def get(self, request):
        # Variables #####################################
        pincode = int(request.query_params.get("pincode"))
        # List of medicine with all lower case
        medicine = PopularMedicine.objects.filter(pincode__contains=pincode)
        #################################################

        # Popular medicine #############################
        medicine_list = []
        data = []
        for med in medicine:
            # medMap = {
            #     "name": med.name.lower(),
            # }
            data.append(med.name.lower())

        c = Counter(data)
        for word, count in c.items():
            counter = {
                "name": word,
                "count": count,
            }
            medicine_list.append(counter)

        print(data)

        return Response(medicine_list, status=status.HTTP_200_OK)
