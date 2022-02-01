# pylint: disable=missing-module-docstring
# 
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/pharmaService > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

__all__ = ['Medical']

from .list import MedicalViewList
from .search import MedicalSearch
from .views import MedicalView

class Medical(MedicalView, MedicalSearch, MedicalViewList):
    """views.medical"""