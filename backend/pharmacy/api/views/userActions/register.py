# pylint: disable=missing-module-docstring
#
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/pharmaService > project,
# and is released under the "BSD 3-Clause License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.


from telnetlib import STATUS
from django.http import JsonResponse

from pharmacy.api.views.userActions.token import serializer
from ...serializers import RegisterSerializer, UserNameSerializer

# Imports for registering a new user
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import status



class Register(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    """
    CreateAPIView is a generic class-based view that allows you to handle POST requests.

    This class is used to register a new user.
    """

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            account.set_active = True

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserNameAvailable(generics.CreateAPIView):
    serializer_class = UserNameSerializer

    # show if username is not available
    def get(self, request):
        queryset = User.objects.all()
        username = request.query_params.get('username', None)
        if username:
            if queryset.filter(username=username).exists():
                return Response({
                    "status": "Username is not available"
                }, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({
                    "status": "Username is available",
                }, status=status.HTTP_200_OK)
        return JsonResponse({
            "status": "Please send a GET request to this endpoint with a query parameter 'username'",
            "example": "GET /api/register/search/?username=your_username",
        })
