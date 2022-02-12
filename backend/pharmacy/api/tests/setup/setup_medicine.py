# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/PharmaService > project,
# and is released under the "BSD 3-Clause License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

from unicodedata import name
from django.contrib.auth.models import User


from rest_framework.test import APIRequestFactory, APITestCase, APIClient


class setupMedicine:
    def medicineTemplate(medicalId: int):
        return {
            "name": "TestMedicine",
            "description": "TestMedicine Description",
            "price": 100,
            "quantity": 100,
            "medicalId": medicalId,
        }

    def setupMedicineForAShop(client: APIClient, header: str, medicalId: int, **kwargs):

        # Extract the payload
        name: str = kwargs.get("name")
        description: str = kwargs.get("description")
        price: int = kwargs.get("price")
        quantity: int = kwargs.get("quantity")

        # Payload
        payload = {
            "name": name != None and name or "TestMedicine",
            "description": description != None
            and description
            or "Test Medicine Description",
            "price": price != None and price or 100,
            "quantity": quantity != None and quantity or 100,
            "medicalId": medicalId,
        }

        return client.post("/api/medicine/", payload, HTTP_AUTHORIZATION=header)
