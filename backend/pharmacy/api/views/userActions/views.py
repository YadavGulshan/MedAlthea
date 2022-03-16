# pylint: disable=missing-module-docstring
#
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/pharmaService > project,
# and is released under the "BSD 3-Clause License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User

from pharmacy.api.serializers import UserSerializer


@permission_classes([IsAuthenticated])
class UserView(APIView):
    def get(self, request, format=None):
        current_user = request.user
        user = User.objects.filter(pk=current_user.id)
        # user = {
        #     "id": current_user.id,
        #     "username": current_user.username,
        #     "email": current_user.email,
        # }
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(user, status=status.HTTP_200_OK)
