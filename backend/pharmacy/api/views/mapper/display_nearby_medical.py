# pylint: disable=missing-module-docstring
#
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/pharmaService > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

from rest_framework.views import APIView
from rest_framework.response import Response


class DisplayNearbyMedical(APIView):
    """
    This class will use distance api endpoint 
    and check for lat and log of medicals listed and then it will show them
    """

    def get(self, request):
        """
        This method will throw the syntax of the required json input
        """

        return Response({
            "status": "Please send a POST request to this endpoint.",
            "example": {
                "lat": "user latitude",
                "lon": "user longitude"
            }
        })
