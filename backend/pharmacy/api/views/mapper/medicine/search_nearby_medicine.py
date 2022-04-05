# pylint: disable=missing-module-docstring
#
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/pharmaService > project,
# and is released under the "BSD 3-Clause License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

import json
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from pharmacy.api.serializers import MedicineSerializer
from pharmacy.api.tools import tools

from pharmacy.models import Medical, Medicine


@permission_classes([IsAuthenticated])
class DisplayNearbyMedicineSearchedByUser(APIView):
    """
    This class will use distance api endpoint
    and check for lat and long of medicals listed and then it will show them
    """
    def get(self, request):
        name = request.query_params.get("name")
        pincode = request.query_params.get("pincode")
        latitude = float(request.query_params.get("latitude"))
        longitude = float(request.query_params.get("longitude"))
        medicineMedical = Medicine.objects.filter(name__contains=name)

        # Check for the pincode of the medicals and then we will show the medicals
        # which are near to the user
        medical = []
        for med in medicineMedical:
            medid = med.medicalId.medicalId
            print("####################ID: ",medid)
            # result = Medical.objects.filter(id=id).filter(
            #         pincode__contains=pincode)
            result = Medical.objects.filter(medicalId=medid).filter(
                pincode__contains=pincode)
            # Calculate the distance between the user and the medical
            for res in result:
                distance = tools.calculate(
                    lat1=latitude,
                    lon1=longitude,
                    lat2=res.latitude,
                    lon2=res.longitude,
                )
                if distance < 2:
                    # medMap = {
                    #     med,
                    #     distance
                    # }
                    # medical[medid] = medMap
                    medical.append(med)

        serializer = MedicineSerializer(medical, many=True)
        return Response(serializer.data, status=200)


    def post(self, request):
        """
        This method will check the request for given pincode and will throw the medicals having pincode similar to request
        """
        pincode = request.data.get("pincode")
        name = request.data.get("name")
        medicineMedical = Medicine.objects.filter(name__contains=name)

        # Now we have to check for the pincode of the medicals and then we will show the medicals
        # which are near to the user
        medical = []
        for med in medicineMedical:
            id = med.medicalId
            # print("search func: ", id.name)
            # print(Medical.objects.get(pincode=id.pincode))
            # Look for id in medical model
            # and then check for the pincode
            result = Medical.objects.filter(pincode=id.pincode).filter(
                pincode__contains=pincode
            )
            # print("result: ", result)
            if result:
                medical.append(med)
        serializer = MedicineSerializer(medical, many=True)
        return Response(serializer.data, status=200)
