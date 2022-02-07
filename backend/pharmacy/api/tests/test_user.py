# pylint: disable=missing-module-docstring
#
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/pharmaService > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.


from random import random
from django.contrib.auth.models import User


from rest_framework.test import APIRequestFactory, APITestCase, APIClient


class userAuthTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()

        for i in range(10):
            User.objects.create_user(
                username='testuser' + str(i),
                password='top_secret' + str(i),
                email='testuser' + str(i) + '@email.com',
                first_name='test',
                last_name='user'
            )

    def test_user_login(self):
        response = self.client.post(
            '/api/token/', {'username': 'testuser1', 'password': 'top_secret1'})
        self.assertEqual(response.status_code, 200)

    def test_unauthenticated_user(self):
        response = self.client.post(
            '/api/token/', {'username': 'testuser1', 'password': 'wrong_password'})
        self.assertEqual(response.status_code, 401)

    def test_username_exist(self):
        response = self.client.get('/api/register/search/?username=testuser1')
        self.assertEqual(response.status_code, 302)

    def test_username_not_exist(self):
        response = self.client.get('/api/register/search/?username=testuser')
        self.assertEqual(response.status_code, 204)

    def test_user_create_medical_shops(self):
        for i in range(10):
            # Login and get the access token
            response = self.client.post(
                '/api/token/', {
                    'username': 'testuser' + str(i),
                    'password': 'top_secret' + str(i)
                }
            )

            access_token = response.data['access']
            # print(access_token)
            self.assertEqual(response.status_code, 200)

            # Create a medical shop
            response = self.client.post('/api/', {
                'name': 'TestUser' + str(i),
                'address': 'TestUser Medical Shop Address' + str(i),
                'pincode': 400607,
                'phone': '+91123456789'+str(i),
                'latitude': random(),
                'longitude': random(),
                'email': 'testuser' + str(i) + '@email.com',
                'website': 'https://testuser' + str(i) + '.com',
            }, HTTP_AUTHORIZATION='Bearer ' + access_token)
            self.assertEqual(response.status_code, 201)

        # Get all the medical shops
        response = self.client.get(
            '/api/', HTTP_AUTHORIZATION='Bearer ' + access_token)
        self.assertEqual(response.status_code, 200)

    def test_user_create_medical_shops_without_token(self):
        response = self.client.post('/api/', {
            'name': 'TestUser',
            'address': 'TestUser Medical Shop Address',
            'pincode': 400607,
            'phone': '+91123456789',
            'latitude': random(),
            'longitude': random(),
            'email': 'testuser' + '@email.com',
            'website': 'https://testuser' + '.com',
        })
        self.assertEqual(response.status_code, 401)

    def test_user_create_medical_shops_with_token_without_data(self):
        '''Login and then perform the post'''
        response = self.client.post(
            '/api/token/', {'username': 'testuser1', 'password': 'top_secret1'})
        access_token = response.data['access']

        response = self.client.post(
            '/api/', {}, HTTP_AUTHORIZATION='Bearer ' + access_token)
        self.assertEqual(response.status_code, 406)

    def test_user_create_medicine(self):
        response = self.client.post(
            '/api/token/', {
                'username': 'testuser1',
                'password': 'top_secret1'
            }
        )
        access_token = response.data['access']

        response = self.client.post('/api/medicine/', {
            'name': 'TestMedicine',
            'description': 'TestMedicine Description',
            'price': 100,
            'quantity': 100,
            'medicalId': 2
        }, HTTP_AUTHORIZATION='Bearer ' + access_token)
        print(response.data)

        # self.assertEqual(response.status_code, 201)

    def test_user_create_medicine_without_token(self):
        response = self.client.post('/api/medicine/', {
            'name': 'TestMedicine',
            'description': 'TestMedicine Description',
            'price': 100,
            'quantity': 100,
        })
        self.assertEqual(response.status_code, 401)
