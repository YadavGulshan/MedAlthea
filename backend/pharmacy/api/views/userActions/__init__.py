# pylint: disable=missing-module-docstring
#
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/pharmaService > project,
# and is released under the "BSD 3-Clause License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.


__all__ = ["UserActions"]

from .token import MyToken
from .register import Register
from .views import UserView
from .activate import Activate


class UserAction(MyToken, Register, UserView, Activate):
    """
    User Actions for registering,
    getting the user info using access token
    and also for generating the jwt token with user details in it..."""
