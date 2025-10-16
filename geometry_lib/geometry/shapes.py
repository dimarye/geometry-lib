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
