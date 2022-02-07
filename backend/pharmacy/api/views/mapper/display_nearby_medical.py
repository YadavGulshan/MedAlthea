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
from pharmacy.api.serializers import MedicalSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from pharmacy.models import Medical

@permission_classes([IsAuthenticated])
class DisplayNearbyMedical(APIView):
    """
    This class will use distance api endpoint 
    and check for lat and log of medicals listed and then it will show them
    """
    def post(self, request):
        """
        This method will check the request for given pincode and will throw the medicals having pincode similar to request
        """
        pincode = request.data.get('pincode')
        medical = Medical.objects.filter(pincode__contains=pincode)
        """
        Here we are checking the pincode of medicals similar to request pincode
        """
        serializer = MedicalSerializer(medical, many=True)
        return Response(serializer.data, status=200)
