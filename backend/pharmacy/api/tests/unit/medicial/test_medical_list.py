# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/PharmaService > project,
# and is released under the "BSD 3-Clause License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

from random import random

from rest_framework.test import APITestCase

from pharmacy.api.tests.setup import Service


class CreateAndGetMedicals(APITestCase):
    def setUp(self):
        self.factory, self.client, self.header = Service.setup_auth_user()

    def test_create_medical_shops(self):
        # Create a medical shop
        response = Service.setupMedicalShop(self.client, self.header)
        self.assertEqual(response.status_code, 201)

    def test_user_create_medical_shops_without_token(self):
        response = self.client.post("/api/", Service.medicalShopTemplate())
        self.assertEqual(response.status_code, 401)

    def test_user_create_medical_shops_with_token_without_data(self):
        response = self.client.post("/api/", HTTP_AUTHORIZATION=self.header)
        self.assertEqual(response.status_code, 406)

    def test_get_list_of_medical(self):
        response = self.client.get("/api/", HTTP_AUTHORIZATION=self.header)
        self.assertEqual(response.status_code, 200)

    def test_get_list_of_medical_without_token(self):
        response = self.client.get("/api/")
        self.assertEqual(response.status_code, 401)
