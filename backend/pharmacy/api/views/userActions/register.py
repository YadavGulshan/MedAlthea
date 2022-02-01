# pylint: disable=missing-module-docstring
# 
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/pharmaService > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.


from ...serializers import RegisterSerializer

# Imports for registering a new user
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

class Register(generics.CreateAPIView):
    """
    CreateAPIView is a generic class-based view that allows you to handle POST requests.

    This class is used to register a new user.
    """

    queryset = User.objects.all()
    """
    Queryset is used to get all the users
    """

    permission_classes = (AllowAny,)
    """
    Allow only unauthenticated users to access this view
    """

    serializer_class = RegisterSerializer
    """
    Now registering the serializer we created in serializers.py
    """
