# pylint: disable=missing-module-docstring
#
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/pharmaService > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.


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
        return Response({
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
    queryset = User.objects.all()

    # show if username is not available
    def get(self, request):
        username = request.GET.get('search')
        if username:
            if self.queryset.filter(username=username).exists():
                return Response({
                    "status": "Username is not available"
                }, status=302)
            else:
                return Response({
                    "status": "Username is available",
                }, status=204)
        return Response({
            "status": "Please send a GET request to this endpoint with a query parameter 'search'"
        })
