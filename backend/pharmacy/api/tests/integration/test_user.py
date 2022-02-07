from urllib import response
from django.contrib.auth.models import User


from rest_framework.test import APIRequestFactory, APITestCase, APIClient


class TestUser(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()

        self.user = User.objects.create_user(
            username="testuser",
            password="top_secret",
            email="testuser@email.com",
            first_name="test",
            last_name="user",
        )

        response = self.client.post(
            "/api/token/", {"username": "testuser", "password": "top_secret"}
        )

        self.access_token = response.data['access']
        self.refresh_token = response.data['refresh']

    def test_user_token_verification(self):
        response = self.client.post(
            "/api/token/verify/", {
                "token": self.access_token
            }
        )
        self.assertEqual(response.status_code, 200)

    def test_user_token_refresh(self):
        response = self.client.post(
            "/api/token/refresh/", {
                "refresh": self.refresh_token
            }
        )
        new_access_token = response.data['access']
        new_refresh_token = response.data['refresh']
        self.assertEqual(response.status_code, 200)

        try_old_refresh_token = self.client.post(
            "/api/token/refresh/", {
                "refresh": self.refresh_token
            }
        )

        self.assertEqual(try_old_refresh_token.status_code, 401)

        try_old_access_token = self.client.post("/api/token/verify/", {
            "token": self.access_token
        })
        # This will pass because the life span of access token is 15 min.
        self.assertEqual(try_old_access_token.status_code, 200)

        try_new_access_token = self.client.post("/api/token/verify/", {
            "token": new_access_token
        })

        self.assertEqual(try_new_access_token.status_code, 200)

    def test_check_user(self):
        response = self.client.get(
            "/api/user/", HTTP_AUTHORIZATION="Bearer " + self.access_token
        )

        self.assertEqual(response.status_code, 200)
