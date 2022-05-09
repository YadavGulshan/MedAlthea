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
from pharmacy.api.views.userActions.token import serializer


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

    def delete(self, request, format=None):
        current_user = request.user
        user = User.objects.filter(pk=current_user.id)
        user.delete()
        return Response("user is deleted!", status=status.HTTP_204_NO_CONTENT)



class UserStatus(APIView):
    def get(self, request):
        username = request.query_params.get("username", None)
        if username:
            user = User.objects.all().filter(username=username)
            # if user is active then return true
            if user.exists():
                serializer = UserSerializer(user, many=True)
                if serializer.data[0]["is_active"] == True:
                    return Response({"status: True"}, status=status.HTTP_200_OK)
                else:
                    return Response({"status: False"}, status=status.HTTP_302_FOUND)
            else:
                return Response({"status": "user does't exists"}, status=status.HTTP_404_NOT_FOUND)