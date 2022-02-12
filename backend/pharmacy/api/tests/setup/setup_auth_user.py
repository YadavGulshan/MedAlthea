from django.contrib.auth.models import User


from rest_framework.test import APIRequestFactory, APITestCase, APIClient


class setup:
    def setup_auth_user(**kwargs):
        factory = APIRequestFactory()
        client = APIClient()

        username = str(
            kwargs.get("username") != None and kwargs.get("username") or "testuser",
        )
        password = str(
            kwargs.get("password") != None and kwargs.get("password") or "top_secret",
        )
        email = str(
            kwargs.get("email") != None
            and kwargs.get("email")
            or "testemail@email.com",
        )
        first_name = str(
            kwargs.get("first_name") != None and kwargs.get("first_name") or "Test",
        )
        last_name = str(
            kwargs.get("last_name") != None and kwargs.get("last_name") or "User",
        )

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_staff=True,
        )
        response = client.post(
            "/api/token/", {"username": username, "password": password}
        )
        access_token = response.data["access"]
        header = "Bearer " + access_token

        return factory, client, header
