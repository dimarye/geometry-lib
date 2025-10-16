import math
import pytest
from geometry_lib.geometry.shapes import Circle, Shape


def test_circle_inherits_from_shape():
    """Test that Circle is a subclass of Shape."""
    assert issubclass(Circle, Shape)


def test_circle_area():
    """Test the area calculation of a circle."""
    radius = 5.0
    circle = Circle(radius)
    expected_area = math.pi * radius ** 2
    assert math.isclose(circle.area(), expected_area)


def test_circle_negative_radius():
    """Test that creating a circle with negative radius raises ValueError."""
    with pytest.raises(ValueError, match="Radius must be positive"):
        Circle(-1.0)


def test_circle_zero_radius():
    """Test that creating a circle with zero radius raises ValueError."""
    with pytest.raises(ValueError, match="Radius must be positive"):
        Circle(0.0)


def test_circle_str_representation():
    """Test the string representation of a Circle."""
    circle = Circle(3.5)
    assert str(circle) == "Circle()"
    assert repr(circle) == "Circle()"
