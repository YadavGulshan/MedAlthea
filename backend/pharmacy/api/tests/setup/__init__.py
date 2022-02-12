__all__ = ['setupService']

from .setup_auth_user import setup
from .setup_medical_shop import setupMedical
class Service(setup, setupMedical):
    """setup"""