"""
Utility functions for geometric calculations.
"""
from typing import Any
from .shapes import Shape


def calculate_area(shape: Shape) -> float:
    """
    Calculate the area of a shape using polymorphism.
    
    Args:
        shape: An object that inherits from Shape class.
        
    Returns:
        The area of the shape.
        
    Raises:
        TypeError: If the provided object is not a Shape.
    """
    if not isinstance(shape, Shape):
        raise TypeError("Object must inherit from Shape")
    return shape.area()
