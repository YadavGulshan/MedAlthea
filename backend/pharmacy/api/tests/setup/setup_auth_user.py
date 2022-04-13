# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/PharmaService > project,
# and is released under the "BSD 3-Clause License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

from django.contrib.auth.models import User


from rest_framework.test import APIClient, APIRequestFactory


class setup:
    def setup_auth_user(**kwargs):
        factory = APIRequestFactory()
        client = APIClient()

        username = str(
            kwargs.get("username") is not None and kwargs.get("username") or "testuser",
        )
        password = str(
            kwargs.get("password") is not None
            and kwargs.get("password")
            or "top_secret",
        )
        email = str(
            kwargs.get("email") is not None
            and kwargs.get("email")
            or "testemail@email.com",
        )
        first_name = str(
            kwargs.get("first_name") is not None and kwargs.get("first_name") or "Test",
        )
        last_name = str(
            kwargs.get("last_name") is not None and kwargs.get("last_name") or "User",
        )

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_staff=True,
        )
        response = client.post(
            "/api/token/", {"username": username, "password": password}
        )
        access_token = response.data["access"]
        header = "Bearer " + access_token

        return factory, client, header

    def setup_auth_user_with_no_staff_permission(**kwargs):
        factory = APIRequestFactory()
        client = APIClient()

        username = str(
            kwargs.get("username") is not None
            and kwargs.get("username")
            or "fuckingstaff",
        )
        password = str(
            kwargs.get("password") is not None
            and kwargs.get("password")
            or "top_secret",
        )
        email = str(
            kwargs.get("email") is not None
            and kwargs.get("email")
            or "testnonstaff@email.com",
        )
        first_name = str(
            kwargs.get("first_name") is not None and kwargs.get("first_name") or "NotA",
        )
        last_name = str(
            kwargs.get("last_name") is not None and kwargs.get("last_name") or "Staff",
        )

        User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_staff=False,
        )

        response = client.post(
            "/api/token/", {"username": username, "password": password}
        )
        access_token = response.data["access"]
        header = "Bearer " + access_token

        return factory, client, header
