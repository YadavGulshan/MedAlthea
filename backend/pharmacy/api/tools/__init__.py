from .smtp_server import smtp_server
from .distance_calculator import CalculateDistanceBetweenTwoPoints
__all__ = ['tools']

class tools(smtp_server, CalculateDistanceBetweenTwoPoints):
    """Tools of our server"""