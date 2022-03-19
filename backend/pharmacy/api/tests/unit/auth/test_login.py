# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/PharmaService > project,
# and is released under the "BSD 3-Clause License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.


from rest_framework.test import APITestCase

from pharmacy.api.tests.setup import Service
class userLoginTest(APITestCase):
    def setUp(self):
        self.factory, self.client, self.header = Service.setup_auth_user()

    def test_user_login(self):
        """User login is already performed by the above setup... 
            This is just ensuring that performing a get request on /token/ does not works
        """
        response = self.client.get("/api/token/", HTTP_AUTHORIZATION=self.header)
        self.assertEqual(response.status_code, 405)

    def test_user_login_without_token(self):
        response = self.client.get("/api/token/")
        self.assertEqual(response.status_code, 405)

    def test_user_data(self):
        response = self.client.get("/api/user/", HTTP_AUTHORIZATION=self.header)
        self.assertEqual(response.status_code, 200)