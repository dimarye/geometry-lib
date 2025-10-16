"""
Tests for utility functions in the geometry package.
"""
import math
import pytest
from geometry_lib.geometry import calculate_area, Circle, Triangle


def test_calculate_area_with_circle():
    """Test calculate_area with Circle instances."""
    # Test with radius = 1 (area = π)
    circle = Circle(1.0)
    assert math.isclose(calculate_area(circle), math.pi)
    
    # Test with radius = 2.5 (area = π * 2.5²)
    circle = Circle(2.5)
    assert math.isclose(calculate_area(circle), math.pi * 2.5 ** 2)


def test_calculate_area_with_triangle():
    """Test calculate_area with Triangle instances."""
    # Right-angled triangle (3-4-5)
    triangle1 = Triangle(3, 4, 5)
    assert math.isclose(calculate_area(triangle1), 6.0)
    
    # Equilateral triangle (side = 2)
    triangle2 = Triangle(2, 2, 2)
    expected_area = math.sqrt(3)  # (√3 * side²) / 4
    assert math.isclose(calculate_area(triangle2), expected_area, rel_tol=1e-9)


def test_calculate_area_with_invalid_type():
    """Test calculate_area with non-Shape objects."""
    with pytest.raises(TypeError, match="Object must inherit from Shape"):
        calculate_area("not a shape")  # type: ignore
    
    with pytest.raises(TypeError, match="Object must inherit from Shape"):
        calculate_area(42)  # type: ignore


class CustomShape:
    """A class that doesn't inherit from Shape but has an area method."""
    def area(self):
        return 42.0


def test_calculate_area_with_non_shape_but_has_area():
    """Test that calculate_area only works with Shape subclasses, even if the object has an area method."""
    custom = CustomShape()
    with pytest.raises(TypeError, match="Object must inherit from Shape"):
        calculate_area(custom)  # type: ignore
