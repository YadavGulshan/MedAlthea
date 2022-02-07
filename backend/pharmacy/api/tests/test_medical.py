from random import random
from django.contrib.auth.models import User


from rest_framework.test import APIRequestFactory, APITestCase, APIClient


class medicalTest(APITestCase):
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
        response = self.client.post(
            "/api/token/", {"username": "testuser", "password": "top_secret"}
        )
        self.access_token = response.data["access"]

    def test_create_medical_shops(self):
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
        self.assertEqual(response.status_code, 201)

    def test_user_create_medical_shops_without_token(self):
        response = self.client.post(
            "/api/",
            {
                "name": "TestUser",
                "address": "TestUser Medical Shop Address",
                "pincode": 400607,
                "phone": "+91123456789",
                "latitude": random(),
                "longitude": random(),
                "email": "testuser" + "@email.com",
                "website": "https://testuser" + ".com",
            },
        )
        self.assertEqual(response.status_code, 401)

    def test_user_create_medical_shops_with_token_without_data(self):
        response = self.client.post(
            "/api/", {}, HTTP_AUTHORIZATION="Bearer " + self.access_token
        )
        self.assertEqual(response.status_code, 406)
