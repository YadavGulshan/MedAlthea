__all__ = ['functions']

from .getData import getData
from .localdb import LocalDB
from .getRegister import getRegister
from .getLogin import getLogin

class functions(getData, LocalDB, getRegister, getLogin):
    """functions.init"""