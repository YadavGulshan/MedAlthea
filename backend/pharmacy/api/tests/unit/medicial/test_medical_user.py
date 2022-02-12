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


class MedicalOwner(APITestCase):
    def setUp(self):
        self.factory, self.client, self.header = Service.setup_auth_user()
        self.header2 = Service.setup_auth_user(
            username="Pawan",
            email="pawan@email.com",
        )[2]

        # Medical shop for user 1
        Service.setupMedicalShop(self.client, self.header)
        Service.setupMedicalShop(
            self.client,
            self.header,
            name="Pawan Medical",
            email="pawan@email.com",
            phone="+912626333322",
        )

        # Medical shop for user 2, i.e Pawan
        Service.setupMedicalShop(
            client=self.client,
            header=self.header2,
            name="India Medical",
            email="IndiaMedical@email.com",
            phone="+912162262325",
        )

    def test_owner_owns(self):
        response = self.client.get("/api/mymedical/", HTTP_AUTHORIZATION=self.header)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["name"], "Test Medical")
        self.assertNotEqual(response.data[1]["name"], "India Medical")


        response = self.client.get("/api/mymedical/", HTTP_AUTHORIZATION=self.header2)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "India Medical")
        self.assertEqual(response.data[0]["email"], "IndiaMedical@email.com")
        self.assertNotEqual(response.data[0]["phone"], "+912626333322")