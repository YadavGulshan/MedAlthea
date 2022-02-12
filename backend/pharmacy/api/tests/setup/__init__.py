__all__ = ["setupService"]

from .setup_auth_user import setup
from .setup_medical_shop import setupMedical
from .setup_medicine import setupMedicine


class Service(setup, setupMedical, setupMedicine):
    """setup"""
