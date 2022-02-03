# pylint: disable=missing-module-docstring
#
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/pharmaService > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

from cmath import cos, sin, sqrt
from math import atan2
from django.http import JsonResponse
from rest_framework.views import APIView


class CalculateDistance(APIView):
    """
    This class is used to calculate the distance between two points
    """

    def get(self, request):
        """
        This method will throw the syntax of the required json input
        """
        return JsonResponse({
            "status": "Please send a POST request to this endpoint.",
            "examples": {
                "lat1": "latitude1",
                "lon1": "longitude1",
                "lat2": "latitude2",
                "lon2": "longitude2",
            }
        })

    def post(self, request):
        """
        This method will calculate the distance between two points
        """
        lat1 = request.data.get('lat1')
        lon1 = request.data.get('lon1')
        lat2 = request.data.get('lat2')
        lon2 = request.data.get('lon2')

        radius = 6371  # km
        dlat = (lat2 - lat1) * (3.14 / 180)
        """
        dlat is the difference between latitude of two points
        """
        dlon = (lon2 - lon1) * (3.14 / 180)
        """
        dlon is the difference between longitude of two points
        """

        O_rad_lat = (lat1 * 3.14 / 180)
        O_rad_lon = (lon1 * 3.14 / 180)

        D_rad_lat = (lat2 * 3.14 / 180)
        D_rad_lon = (lon2 * 3.14 / 180)

        a = (sin(dlat/2)*sin(dlat/2) + cos(O_rad_lat)
             * cos(D_rad_lat)*sin(dlon/2)*sin(dlon/2))
        """
        a is the value of the formula
        

        we are using haversine formula to calculate the distance between two points
        maths formula:
            a = sin²(Δφ/2) + cos(φ1).cos(φ2).sin²(Δλ/2)
            c = 2.atan2(√a, √(1−a))
            d = R.c
        """

        c = 2*atan2(sqrt(a), sqrt(1-a))
        d = radius*c
        """
        d is the distance between two points
        """

        return JsonResponse({
            "distance": d,
        })
