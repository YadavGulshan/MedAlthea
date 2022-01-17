# pylint: disable=missing-module-docstring
# 
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/PharmaServiceBackend > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaServiceBackend/blob/master/LICENCE >
#
# All rights reserved.

__all__ = ['app']

from flask import Flask
app = Flask(__name__)