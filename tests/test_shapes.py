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


def test_triangle_inherits_from_shape():
    """Test that Triangle is a subclass of Shape."""
    from geometry_lib.geometry.shapes import Triangle
    assert issubclass(Triangle, Shape)


def test_triangle_creation():
    """Test creating a valid triangle."""
    triangle = Triangle(3, 4, 5)
    assert triangle.a == 3
    assert triangle.b == 4
    assert triangle.c == 5


def test_triangle_invalid_sides():
    """Test that invalid triangle sides raise ValueError."""
    with pytest.raises(ValueError, match="Invalid triangle sides"):
        Triangle(1, 1, 3)  # 1 + 1 <= 3
    with pytest.raises(ValueError, match="Invalid triangle sides"):
        Triangle(0, 1, 1)  # Zero side
    with pytest.raises(ValueError, match="Invalid triangle sides"):
        Triangle(-1, 2, 2)  # Negative side


def test_triangle_area():
    """Test the area calculation of a triangle."""
    # Right-angled triangle
    triangle1 = Triangle(3, 4, 5)
    assert math.isclose(triangle1.area(), 6.0)
    
    # Equilateral triangle
    triangle2 = Triangle(2, 2, 2)
    expected_area = (3 ** 0.5)  # (sqrt(3) * side²) / 4
    assert math.isclose(triangle2.area(), expected_area, rel_tol=1e-9)


def test_triangle_is_right_angle():
    """Test the right-angle checking of a triangle."""
    # Right-angled triangle
    assert Triangle(3, 4, 5).is_right_angle() is True
    assert Triangle(5, 12, 13).is_right_angle() is True
    
    # Not right-angled
    assert Triangle(3, 4, 6).is_right_angle() is False
    assert Triangle(2, 2, 2).is_right_angle() is False  # Equilateral


def test_triangle_str_representation():
    """Test the string representation of a Triangle."""
    triangle = Triangle(3, 4, 5)
    assert str(triangle) == "Triangle(a=3, b=4, c=5)"
    assert repr(triangle) == "Triangle(a=3, b=4, c=5)"
