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
