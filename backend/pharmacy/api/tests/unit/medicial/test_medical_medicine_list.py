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


class CheckMedicalMedicine(APITestCase):
    def setUp(self):
        self.factory, self.client, self.header = Service.setup_auth_user()
        res = Service.setupMedicalShop(client=self.client, header=self.header)
        self.medicalId = res.data["medicalId"]
        Service.setupMedicineForAShop(
            client=self.client, header=self.header, medicalId=self.medicalId
        )

        # Create another user
        self.factory, self.client, self.header2 = Service.setup_auth_user(
            username="user2",
            password="user2",
            email="someemail@gmail.com",
            first_name="user",
            last_name="user",
        )

        res = Service.setupMedicalShop(client=self.client, header=self.header2)
        self.medicalId2 = res.data["medicalId"]
        Service.setupMedicineForAShop(
            client=self.client, header=self.header2, medicalId=self.medicalId2
        )

    def test_medicine_list(self):
        response = self.client.get(
            "/api/mymedical/{}/".format(self.medicalId), HTTP_AUTHORIZATION=self.header
        )
        self.assertEqual(response.status_code, 200)

    def test_if_another_medical_owner_can_see_the_medicine_list(self):
        response = self.client.get(
            "/api/mymedical/{}/".format(self.medicalId2), HTTP_AUTHORIZATION=self.header
        )
        self.assertEqual(response.status_code, 403)
