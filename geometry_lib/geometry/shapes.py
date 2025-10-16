from abc import ABC, abstractmethod
from typing import Optional


class Shape(ABC):
    """
    Abstract base class for all geometric shapes.
    All shapes must implement the area() method.
    """
    
    @abstractmethod
    def area(self) -> float:
        """
        Calculate the area of the shape.
        
        Returns:
            float: The area of the shape.
            
        Raises:
            NotImplementedError: If the subclass doesn't implement this method.
        """
        raise NotImplementedError("Subclasses must implement area() method")
    
    def __str__(self) -> str:
        """Return string representation of the shape."""
        return f"{self.__class__.__name__}()"
    
    def __repr__(self) -> str:
        """Return official string representation of the shape."""
        return str(self)


class Triangle(Shape):
    """A class representing a triangle with three sides."""
    
    def __init__(self, a: float, b: float, c: float) -> None:
        """
        Initialize a triangle with three sides.
        
        Args:
            a: Length of the first side.
            b: Length of the second side.
            c: Length of the third side.
            
        Raises:
            ValueError: If the sides do not form a valid triangle.
        """
        sides = sorted([a, b, c])
        if sides[0] <= 0 or sides[0] + sides[1] <= sides[2]:
            raise ValueError("Invalid triangle sides")
        self.a, self.b, self.c = sides
    
    def area(self) -> float:
        """
        Calculate the area of the triangle using Heron's formula.
        
        Returns:
            The area of the triangle.
        """
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
    
    def is_right_angle(self) -> bool:
        """
        Check if the triangle is right-angled.
        
        Returns:
            True if the triangle is right-angled, False otherwise.
        """
        return abs(self.a**2 + self.b**2 - self.c**2) < 1e-9
    
    def __str__(self) -> str:
        """Return string representation of the triangle."""
        return f"{self.__class__.__name__}(a={self.a}, b={self.b}, c={self.c})"
    
    def __repr__(self) -> str:
        """Return official string representation of the triangle."""
        return str(self)


class Circle(Shape):
    """A class representing a circle with a given radius."""
    
    def __init__(self, radius: float):
        """
        Initialize a circle with the given radius.
        
        Args:
            radius: The radius of the circle. Must be positive.
            
        Raises:
            ValueError: If radius is not positive.
        """
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius
    
    def area(self) -> float:
        """
        Calculate the area of the circle.
        
        Returns:
            The area of the circle (π * radius²).
        """
        from math import pi
        return pi * self.radius ** 2
