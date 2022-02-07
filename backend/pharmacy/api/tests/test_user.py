# pylint: disable=missing-module-docstring
#
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/pharmaService > project,
# and is released under the "BSD 3-Clause License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.


from urllib import response
from django.contrib.auth.models import User


from rest_framework.test import APIRequestFactory, APITestCase, APIClient


class userAuthTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()

        self.user = User.objects.create_user(
            username="testuser",
            password="top_secret",
            email="testuser@email.com",
            first_name="test",
            last_name="user",
        )

    def test_user_login(self):
        response = self.client.post(
            "/api/token/", {"username": "testuser", "password": "top_secret"}
        )
        self.assertEqual(response.status_code, 200)

    def test_unauthenticated_user(self):
        response = self.client.post(
            "/api/token/", {"username": "testuser1",
                            "password": "wrong_password"}
        )
        self.assertEqual(response.status_code, 401)

    def test_username_exist(self):
        response = self.client.get("/api/register/search/?username=testuser")
        self.assertEqual(response.status_code, 400)

    def test_username_not_exist(self):
        response = self.client.get("/api/register/search/?username=testuser1")
        self.assertEqual(response.status_code, 200)
