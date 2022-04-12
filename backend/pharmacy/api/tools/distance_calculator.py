# pylint: disable=missing-module-docstring
#
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/pharmaService > project,
# and is released under the "BSD 3-Clause License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

from cmath import cos, sin, sqrt
from math import atan2


class CalculateDistanceBetweenTwoPoints:
    def calculate(lat1: float, lon1: float, lat2: float, lon2: float):
        radius = 6371
        dlat = (lat2 - lat1) * (3.14 / 180)
        dlon = (lon2 - lon1) * (3.14 / 180)

        O_rad_lat = lat1 * 3.14 / 180
        O_rad_lon = lon1 * 3.14 / 180

        D_rad_lat = lat2 * 3.14 / 180
        D_rad_lon = lon2 * 3.14 / 180

        a = sin(dlat / 2) * sin(dlat / 2) + cos(O_rad_lat) * cos(D_rad_lat) * sin(
            dlon / 2
        ) * sin(dlon / 2)

        a = a.real
        c = 2 * atan2(sqrt(a).real, sqrt(1 - a).real)
        d = radius * c

        return d
