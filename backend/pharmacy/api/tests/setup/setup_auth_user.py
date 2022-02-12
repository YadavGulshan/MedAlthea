from django.contrib.auth.models import User


from rest_framework.test import APIRequestFactory, APITestCase, APIClient


class setup:
    
    def setup_auth_user(self):
        factory = APIRequestFactory()
        client = APIClient()
        user = User.objects.create_user(
            username="testuser",
            password="top_secret",
            email="testuser@email.com",
            first_name="test",
            last_name="user",
            is_staff=True,
        )
        response = client.post(
            "/api/token/", {"username": "testuser", "password": "top_secret"}
        )
        access_token = response.data["access"]
        header = "Bearer " + access_token

        return factory, client, header