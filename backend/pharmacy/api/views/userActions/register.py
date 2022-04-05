# pylint: disable=missing-module-docstring
#
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/pharmaService > project,
# and is released under the "BSD 3-Clause License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.


from base64 import urlsafe_b64encode
from django.http import JsonResponse
from pharmacy.api.tools import tools
from pharmacy.api.views.userActions.token.token_generator import TokenGenerator

from ...serializers import RegisterSerializer, UserNameSerializer

# Imports for registering a new user
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from django.utils.encoding import force_bytes


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
            if "isStaff" not in request.data:
                account.is_staff = False

            if "isStaff" in request.data:
                if request.data["isStaff"]:
                    account.is_staff = True

            # Set the user to inactive
            account.is_active = False
            account.save()
            # Abstract base user
            user = User.objects.get(username=account.username)
            tokengen = TokenGenerator()
            uid = urlsafe_b64encode(force_bytes(user.pk))
            token = tokengen.make_token(user)
            print(
                str(
                    str("http://localhost:8000/api/emailverification/")
                    + str(uid).replace("b", "").replace("'", "")
                    + "/"
                    + str(token)
                )
            )
            tools.send_email(
                send_to=request.data["email"],
                url=str(
                    str("http://localhost:8000/api/emailverification/")
                    + str(uid).replace("b", "").replace("'", "")
                    + "/"
                    + str(token)
                    + "/"
                ),
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserNameAvailable(generics.CreateAPIView):
    serializer_class = UserNameSerializer

    # show if username is not available
    def get(self, request):
        queryset = User.objects.all()
        username = request.query_params.get("username", None)
        if username:
            if queryset.filter(username=username).exists():
                return Response(
                    {"status": "Username is not available"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            else:
                return Response(
                    {
                        "status": "Username is available",
                    },
                    status=status.HTTP_200_OK,
                )
        return JsonResponse(
            {
                "status": "Please send a GET request to this endpoint with a query parameter 'username'",
                "example": "GET /api/register/search/?username=your_username",
            }
        )
