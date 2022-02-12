# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/PharmaService > project,
# and is released under the "BSD 3-Clause License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

from random import random
from urllib import response
from black import diff

from rest_framework.test import APITestCase

from pharmacy.api.tests.setup import Service


class MedicalView(APITestCase):
    def setUp(self):

        # User 1
        self.factory, self.client, self.header = Service.setup_auth_user()

        # Medical shop for user 2
        Service.setupMedicalShop(self.client, self.header)
        Service.setupMedicalShop(
            self.client,
            self.header,
            name="tasty Medical",
            email="tasty@email.com",
            phone="+912626333322",
        )

        # Second User
        self.header2 = Service.setup_auth_user(
            username="Pawan",
            email="pawan@email.com",
        )[2]

        # Medical shop for user 2, i.e Pawan
        Service.setupMedicalShop(
            client=self.client,
            header=self.header2,
            name="India Medical",
            email="IndiaMedical@email.com",
            phone="+912162262325",
        )

    def test_get_medical_by_id(self):
        response = self.client.get("/api/1/", HTTP_AUTHORIZATION=self.header)
        self.assertEqual(response.data[0]["name"], "Test Medical")

    def test_update_medical_name_by_id(self):
        response = self.client.get("/api/", HTTP_AUTHORIZATION=self.header)
        medId = response.data[0]["medicalId"]

        beforeUpdate = response.data[0]

        # Updating the name of the medical shop
        response = self.client.put(
            "/api/{}/".format(medId),
            {
                "name": "new medical name",
            },
            HTTP_AUTHORIZATION=self.header,
        )

        # Getting the new data
        response = self.client.get("/api/", HTTP_AUTHORIZATION=self.header)
        afterUpdate = response.data[0]

        # Ensure that the name of the medical shop is updated
        self.assertEqual(
            afterUpdate["name"],
            "new medical name",
        )

        # poping the name field
        beforeUpdate.pop("name")
        afterUpdate.pop("name")

        # Ensuring that other fields are not changed
        self.assertEqual(
            beforeUpdate,
            afterUpdate,
        )

    def test_update_email(self):
        response = self.client.get("/api/", HTTP_AUTHORIZATION=self.header)
        medId = response.data[0]["medicalId"]

        # Updating the email of the medical shop
        response = self.client.put(
            "/api/{}/".format(medId),
            {
                "email": "somemedical@email.com",
            },
            HTTP_AUTHORIZATION=self.header,
        )

        self.assertEqual(response.status_code, 400)

    def test_update_phone(self):
        response = self.client.get("/api/", HTTP_AUTHORIZATION=self.header)
        medId = response.data[0]["medicalId"]

        # Updating the phone of the medical shop
        response = self.client.put(
            "/api/{}/".format(medId),
            {
                "phone": "1234567890",
            },
            HTTP_AUTHORIZATION=self.header,
        )

        self.assertEqual(response.status_code, 400)
