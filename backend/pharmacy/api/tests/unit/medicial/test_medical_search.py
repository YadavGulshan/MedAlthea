# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/PharmaService > project,
# and is released under the "BSD 3-Clause License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

from random import random
from urllib import response
from django.contrib.auth.models import User


from rest_framework.test import APITestCase

from pharmacy.api.tests.setup import Service


class SearchMedicalShop(APITestCase):
    def setUp(self):
        self.factory, self.client, self.header = Service.setup_auth_user()
        payload = {
            "name": "Pawan Medical",
            "address": "Pawan Medical Shop Address",
            "pincode": 4565616,
            "phone": "+911234567891",
            "latitude": random(),
            "longitude": random(),
            "email": "pawan" + "@email.com",
            "website": "https://pawan" + ".com",
        }
        Service.setupCustomMedical(
            client=self.client, header=self.header, payload=payload
        )
        Service.setupCustomMedical(
            client=self.client,
            header=self.header,
            payload=Service.medicalShopTemplate(),
        )

    def test_search(self):
        response = self.client.get(
            "/api/search/?search=Medical", format="json", HTTP_AUTHORIZATION=self.header
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

        response = self.client.get(
            "/api/search/?search=Pawan", format="json", HTTP_AUTHORIZATION=self.header
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["name"], "Pawan Medical")
