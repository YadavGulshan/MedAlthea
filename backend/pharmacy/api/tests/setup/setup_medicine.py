# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/PharmaService > project,
# and is released under the "BSD 3-Clause License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.


from rest_framework.test import APIClient


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
        name: str = (
            kwargs.get("name") is not None and kwargs.get("name") or "TestMedicine"
        )
        description: str = (
            kwargs.get("description") is not None
            and kwargs.get("description")
            or "TestMedicine Description"
        )
        price: int = kwargs.get("price") is not None and kwargs.get("price") or 100
        quantity: int = (
            kwargs.get("quantity") is not None and kwargs.get("quantity") or 100
        )

        # Payload
        payload = {
            "name": name,
            "description": description,
            "price": price,
            "quantity": quantity,
            "medicalId": medicalId,
        }

        return client.post("/api/medicine/", payload, HTTP_AUTHORIZATION=header)
