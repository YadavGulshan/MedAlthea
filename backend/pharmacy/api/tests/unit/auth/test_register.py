# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/PharmaService > project,
# and is released under the "BSD 3-Clause License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

from base64 import decode
from rest_framework.test import APITestCase

from pharmacy.api.tests.setup import Service
from django.contrib.auth.models import User



class test_user_registeration(APITestCase):
    def setUp(self):
        self.factory, self.client, self.header = Service.setup_auth_user_with_no_staff_permission()
        User.objects.create_user(
            username = "staffUser",
            password = "top_secret",
            email = "staff@k.com",
            first_name = "Staff",
            last_name = "User",
            is_staff = False,
        )
        response = self.client.post(
            "/api/token/", {"username": "staffUser", "password": "top_secret"}
        )
        access_token = response.data["access"]
        self.header2 = "Bearer " + access_token
        
    def test_user_registeration(self):
        """User registeration is already performed by the above setup... 
            This is just ensuring that performing a post request on /register/ does not works
        """
        response = self.client.post(
            "/api/register/",
            {
                "username": "testuser",
                "password": "top_secret",
                "password2": "top_secret",
                "email": "staff@k.com",
                "first_name": "Test",
                "last_name": "User",
            },
        )
        self.assertEqual(response.status_code, 400)
    
    def test_user_registeration_without_staff_permission(self):
        response = self.client.get("/api/user/", HTTP_AUTHORIZATION=self.header2)
        self.assertEqual(response.status_code, 200)