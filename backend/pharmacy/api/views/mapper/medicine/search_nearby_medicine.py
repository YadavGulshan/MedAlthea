# pylint: disable=missing-module-docstring
#
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/pharmaService > project,
# and is released under the "BSD 3-Clause License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
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
            print("####################ID: ", medid)
            # result = Medical.objects.filter(id=id).filter(
            #         pincode__contains=pincode)
            result = Medical.objects.filter(medicalId=medid).filter(
                pincode__contains=pincode
            )
            for _ in result:
                medical.append(med)
        newData = []
        for med in medical:
            medid = med.medicalId
            medMap = {
                "name": med.name,
                "medical_name": medid.name,
                "price": med.price,
                "description": med.description,
                "quantity": med.quantity,
                "pincode": medid.pincode,
                "latitude": medid.latitude,
                "longitude": medid.longitude,
                "distance": tools.calculate(
                    lat1=latitude,
                    lon1=longitude,
                    lat2=medid.latitude,
                    lon2=medid.longitude,
                ),
            }
            newData.append(medMap)

        # Sort the data according to the distance
        newData.sort(key=lambda x: x["distance"])
        return JsonResponse(newData, safe=False)
