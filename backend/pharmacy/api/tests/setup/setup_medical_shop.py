from random import random
from urllib import response
from django.contrib.auth.models import User


from rest_framework.test import APIClient


class setupMedical:
    def medicalShopTemplate():
        return {
            "name": "Test Medical",
            "address": "TestUser Medical Shop Address",
            "pincode": 400607,
            "phone": "+911234567891",
            "latitude": random(),
            "longitude": random(),
            "email": "testuser" + "@email.com",
            "website": "https://testuser" + ".com",
        }

    def setupMedicalShop(client: APIClient, header: str):
        payload = {
            "name": "TestUser",
            "address": "TestUser Medical Shop Address",
            "pincode": 400607,
            "phone": "+911234567891",
            "latitude": random(),
            "longitude": random(),
            "email": "testuser" + "@email.com",
            "website": "https://testuser" + ".com",
        }
        response = client.post("/api/", payload, HTTP_AUTHORIZATION=header)
        return response

    def setupCustomMedical(client: APIClient, header: str, payload: dict):
        response = client.post("/api/", payload, HTTP_AUTHORIZATION=header)
        return response
