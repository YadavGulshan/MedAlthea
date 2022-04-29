# pylint: disable=missing-module-docstring
#
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/pharmaService > project,
# and is released under the "BSD 3-Clause License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

__all__ = ["Mapper"]

from pharmacy.api.views.mapper.distance import CalculateDistance
from pharmacy.api.views.mapper.popular_medicine import PopularMedicineSearch
from .display_nearby_medical import DisplayNearbyMedical
from .medicine import MedicineSearch


class Mapper(CalculateDistance, DisplayNearbyMedical, MedicineSearch, PopularMedicineSearch):
    """views.mapper"""
