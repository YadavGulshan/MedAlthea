# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/PharmaService > project,
# and is released under the "BSD 3-Clause License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

__all__ = ["setupService"]

from .setup_auth_user import setup
from .setup_medical_shop import setupMedical
from .setup_medicine import setupMedicine


class Service(setup, setupMedical, setupMedicine):
    """setup"""
