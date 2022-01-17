# pylint: disable=missing-module-docstring
#
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/PharmaServiceBackend > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaServiceBackend/blob/master/LICENCE >
#
# All rights reserved.

__all__ = ['Config', 'get_version']

import os
from typing import Set
from git import Repo



class Config:
    MONGO_USERNAME = os.environ.get('MONGO_USERNAME')
    MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')
    CLUSTER_NAME = os.environ.get('CLUSTER_NAME')
    UPSTREAM_REMOTE = os.environ.get('UPSTREAM_REMOTE')
    UPSTREAM_REPO = os.environ.get('UPSTREAM_REPO')
