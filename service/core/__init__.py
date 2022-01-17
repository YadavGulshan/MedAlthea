# pylint: disable=missing-module-docstring
# 
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/PharmaServiceBackend > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaServiceBackend/blob/master/LICENCE >
#
# All rights reserved.

from .database import get_collection
from .client import PharmaService
from .app import app

app.run(debug=True)