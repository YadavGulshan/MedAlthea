# pylint: disable=missing-module-docstring
#
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/pharmaService > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.


from django.contrib.auth.models import User


from rest_framework.test import APIRequestFactory, APITestCase, APIClient


class simpleTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            username='testuser',  password='top_secret', email='testuser@email.com', first_name='test', last_name='user')
        self.user.save()

    def test_user_login(self):
        self.client = APIClient()
        response = self.client.post(
            '/api/token/', {'username': 'testuser', 'password': 'top_secret'})
        self.assertEqual(response.status_code, 200)

    def test_username_exist(self):
        response = self.client.get('/api/register/search/?search=testuser')
        print(response.data)
        self.assertEqual(response.status_code, 200)