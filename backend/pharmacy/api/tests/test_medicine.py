from random import random
from django.contrib.auth.models import User


from rest_framework.test import APIRequestFactory, APITestCase, APIClient


class medicinetest(APITestCase):
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

        # Create a medical shop
        response = self.client.post(
            "/api/",
            {
                "name": "TestUser",
                "address": "TestUser Medical Shop Address",
                "pincode": 400607,
                "phone": "+911234567891",
                "latitude": random(),
                "longitude": random(),
                "email": "testuser" + "@email.com",
                "website": "https://testuser" + ".com",
            },
            HTTP_AUTHORIZATION="Bearer " + self.access_token,
        )
        self.medicalId = response.data["medicalId"]

    def test_user_create_medicine(self):
        response = self.client.get(
            "/api/mymedical/", HTTP_AUTHORIZATION="Bearer " + self.access_token
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            "/api/medicine/",
            {
                "name": "TestMedicine",
                "description": "TestMedicine Description",
                "price": 100,
                "quantity": 100,
                "medicalId": self.medicalId,
            },
            HTTP_AUTHORIZATION="Bearer " + self.access_token,
        )

        self.assertEqual(response.status_code, 201)

    def test_user_create_medicine_without_token(self):
        response = self.client.post(
            "/api/medicine/",
            {
                "name": "TestMedicine",
                "description": "TestMedicine Description",
                "price": 100,
                "quantity": 100,
            },
        )
        self.assertEqual(response.status_code, 401)
