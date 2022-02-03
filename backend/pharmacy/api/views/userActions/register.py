# pylint: disable=missing-module-docstring
#
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/pharmaService > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.


from django.http import JsonResponse
from ...serializers import RegisterSerializer

# Imports for registering a new user
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import filters


class Register(generics.CreateAPIView):
    """
    CreateAPIView is a generic class-based view that allows you to handle POST requests.

    This class is used to register a new user.
    """
    def get(self, request):
        """
        This method will throw the syntax of the required json input
        """
        return JsonResponse({
            "status": "Please send a POST request to this endpoint.",
            "examples": {
                "username": "your_username",
                "email": "your_email@example.com",
                "first_name": "First_Name",
                "last_name": "Last_Name",
            }
        })

    def post(self, request):
        # """
        # This method will register the user
        # """
        # queryset = User.objects.all()
        # """
        # Queryset is used to get all the users
        # """

        # permission_classes = (AllowAny,)
        # """
        # Allow only unauthenticated users to access this view
        # """

        # serializer_class = RegisterSerializer
        # """
        # Now registering the serializer we created in serializers.py
        # """
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            account.set_active = True

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



class UserNameAvailable(generics.ListCreateAPIView):
    search_fields = ['username']
    filter_backends = (filters.SearchFilter,)
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
