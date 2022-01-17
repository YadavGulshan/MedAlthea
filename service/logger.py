# pylint: disable=missing-module-docstring
# 
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/PharmaServiceBackend > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaServiceBackend/blob/master/LICENCE >
#
# All rights reserved.

__all__ = ['Logging']


from cmath import log
import logging
from logging.handlers import RotatingFileHandler


logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s - %(levelname)s] - %(name)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    handlers=[
                        RotatingFileHandler(
                            "logs/PharmaServiceBackend.log",maxBytes=20480, backupCount=10),
                            logging.StreamHandler()
                    ])
                    
logging.getLogger("mongodb").setLevel(logging.WARNING)
logging.getLogger('googleapiclient.discovery').setLevel(logging.WARNING)

