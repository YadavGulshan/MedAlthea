# pylint: disable=missing-module-docstring
#
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/pharmaService > project,
# and is released under the "BSD 3-Clause License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.
from base64 import urlsafe_b64decode
from rest_framework.views import APIView
from rest_framework.response import Response
from pharmacy.api import serializers
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes
from pharmacy.api.tools import tools
from pharmacy.api.views.userActions.token.token_generator import TokenGenerator
from rest_framework import status


class ResetPasswordRequest(APIView):
    """
    To use this serializer, you must pass in the following data:
    ```json
    {
        "email": "email@email.com",
    }
    ```
    Firstly, we need to confirm if the email is allotted to any user.
    If the email is allotted to any user, then we need to send a reset password link to the email.

    The reset password link will contain the token.
    The token will be used to reset the password.
    """

    def post(self, request):
        serializer = serializers.ResetPasswordRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        if serializer.is_valid():
            user = User.objects.filter(email=email).first()
            if user:
                token = TokenGenerator()
                uid = urlsafe_b64decode(force_bytes(user.pk))
                token = token.make_token(user)
                tools.send_email(
                    send_to=email,
                    subject="Reset Password",
                    url=str(
                        str("http://localhost:8000/api/resetpassword/")
                        + str(uid).replace("b", "").replace("'", "")
                        + "/"
                        + str(token)
                        + "/"
                    ),
                )
                return Response(
                    {"message": "Reset password link has been sent to your email."},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"message": "Email is not allotted to any user."},
                    status=status.HTTP_400_BAD_REQUEST,
                )


class Reset(APIView):
    def post(self, request):
        pass

    def get(self, request, uidb64, token):
        pass
