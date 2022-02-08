# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/PharmaService > project,
# and is released under the "BSD 3-Clause License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

from django.contrib.auth.models import User

from random import random
from rest_framework.test import APIRequestFactory, APITestCase, APIClient


class IntegrationTestMedicine(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser",
            password="top_secret",
            email="testuser@email.com",
            first_name="test",
            last_name="user",
            is_staff=True,
        )

        # Login and get the token
        response = self.client.post(
            "/api/token/", {"username": "testuser", "password": "top_secret"}
        )
        self.access_token = response.data["access"]

        # Create a medical shop
        response = self.client.post(
            "/api/",
            {
                "name": "TestUser",
                "address": "TestUser Medical Shop Address",
                "pincode": 400607,
                "phone": "+911234567891",
                "latitude": random(),
                "longitude": random(),
                "email": "testuser" + "@email.com",
                "website": "https://testuser" + ".com",
            },
            HTTP_AUTHORIZATION="Bearer " + self.access_token,
        )
        self.medicalId = response.data["medicalId"]

    def test_create_and_search_medicine(self):
        pass
