# pylint: disable=missing-module-docstring
# 
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/pharmaService > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

import unittest
from django.test import Client

class TestAPI(unittest.TestCase):
    def test_get(self):
        print("Module is {}".format(__name__))
        c = Client()
        response = c.get('/api/')
        self.assertEqual(response.status_code, 200)
