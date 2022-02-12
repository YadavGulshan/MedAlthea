# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/PharmaService > project,
# and is released under the "BSD 3-Clause License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

from django.contrib.auth.models import User

import random
from rest_framework.test import APIRequestFactory, APITestCase, APIClient

from pharmacy.api.tests.data import medicineNames


class IntegrationTestForSearchingMedicineInNearbyMedicalShops(APITestCase):
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

        self.header = "Bearer " + self.access_token

        for i in range(10):
            try:
                medicalShop = self.client.post(
                    "/api/",
                    {
                        "name": "TestUser" + str(i),
                        "address": "TestUser Medical Shop Address",
                        "pincode": "{0:5}".format(random.randint(1, 1000000)),
                        "phone": "+91" + str(random.randint(10**9, 10**10 - 1)),
                        "latitude": random.random(),
                        "longitude": random.random(),
                        "email": "testuser" + str(i) + "@email.com",
                    },
                    HTTP_AUTHORIZATION=self.header,
                )
                GenmedicalId = medicalShop.data["medicalId"]

                for j in range(10):
                    medicine = self.client.post(
                        "/api/medicine/",
                        {
                            "name": medicineNames.medicineNames[
                                random.randint(0, len(medicineNames.medicineNames) - 1)
                            ],
                            "description": "TestMedicine Description",
                            "price": "{0:2}".format(random.randint(1, 100)),
                            "quantity": "{0:2}".format(random.randint(1, 100)),
                            "medicalId": GenmedicalId,
                        },
                        HTTP_AUTHORIZATION=self.header,
                    )
            except KeyError:
                pass

        try:
            testmedicalShop = self.client.post(
                "/api/",
                {
                    "name": "MedicalShop",
                    "address": "TestUser Medical Shop Address",
                    "pincode": 400607,
                    "phone": "+917965656565",
                    "latitude": random.random(),
                    "longitude": random.random(),
                    "email": "someemail@email.com",
                },
                HTTP_AUTHORIZATION=self.header,
            )
            testmedicalId = testmedicalShop.data["medicalId"]

            test_medicine = self.client.post(
                "/api/medicine/",
                {
                    "name": "TestMedicine",
                    "description": "TestMedicine Description",
                    "price": "{0:2}".format(random.randint(1, 100)),
                    "quantity": "{0:2}".format(random.randint(1, 100)),
                    "medicalId": testmedicalId,
                },
                HTTP_AUTHORIZATION=self.header,
            )
        except Exception as e:
            print(e, "at setUp")

    def test_dryrun(self):
        response = self.client.post(
            "/api/nearbymedicine/",
            {
                "pincode": "4006",
                "name": "TestMedicine",
            },
            HTTP_AUTHORIZATION=self.header,
        )
        # print(response.data)
        self.assertEqual(response.status_code, 200)
