"""
Geometry module for geometric calculations.
"""

from .shapes import Shape, Circle, Triangle
from .utils import calculate_area

__all__ = [
    'Shape',
    'Circle',
    'Triangle',
    'calculate_area',
]  # Expose public API at package level
