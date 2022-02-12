# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/PharmaService > project,
# and is released under the "BSD 3-Clause License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.


from rest_framework.test import APITestCase

from pharmacy.api.tests.setup import Service


class medicinetest(APITestCase):
    def setUp(self):
        self.factory, self.client, self.header = Service.setup_auth_user()

        # Create a medical shop
        response = Service.setupMedicalShop(self.client, self.header)
        self.medicalId: int = response.data["medicalId"]

    def test_user_create_medicine(self):
        response = self.client.get("/api/mymedical/", HTTP_AUTHORIZATION=self.header)
        self.assertEqual(response.status_code, 200)

        # Seting up the payload for creating a medicine
        response = Service.setupMedicineForAShop(
            client=self.client,
            header=self.header,
            medicalId=self.medicalId,
            name="DOLO 650",
            description="A Medicine to relieve headache",
            price=32,
            quantity=100,
        )

        self.assertEqual(response.status_code, 201)

    def test_user_create_medicine_without_token(self):
        response = Service.setupMedicineForAShop(
            client=self.client,
            header=None,
            medicalId=self.medicalId,
            name="DOLO 650",
            description="A Medicine to relieve headache",
            price=32,
            quantity=100,
        )
        self.assertEqual(response.status_code, 401)
