# Geometry Library

[![PyPI](https://img.shields.io/pypi/v/geometry-lib)](https://pypi.org/project/geometry-lib/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/pypi/pyversions/geometry-lib)](https://pypi.org/project/geometry-lib/)

A Python library for geometric calculations with support for various shapes, right-angle triangle checking, and polymorphic area calculation.

## Features

- **Circle**: Calculate area of a circle
- **Triangle**: Calculate area and check if it's a right-angled triangle
- **Polymorphic Area Calculation**: Single function to calculate area for any shape
- **Type Hints**: Full type support for better IDE integration
- **Input Validation**: Ensures geometric validity of shapes

## Installation

```bash
pip install geometry-lib
```

Or install from source:

```bash
git clone https://github.com/dimarye/geometry-lib.git
cd geometry-lib
pip install -e .
```

## Usage

```python
from geometry_lib.geometry import Circle, Triangle, calculate_area

# Create shapes
circle = Circle(3)      # Radius = 3
triangle = Triangle(3, 4, 5)  # Sides 3, 4, 5

# Calculate areas
print(f"Circle area: {calculate_area(circle):.2f}")      # 28.27
print(f"Triangle area: {calculate_area(triangle)}")      # 6.0

# Check if triangle is right-angled
print(f"Is right-angled: {triangle.is_right_angle()}")   # True
```

### Advanced Usage

```python
# Create a list of different shapes
shapes = [
    Circle(5),
    Triangle(6, 8, 10),
    Circle(2.5),
    Triangle(5, 5, 5)  # Equilateral triangle
]

# Calculate total area of all shapes
total_area = sum(calculate_area(shape) for shape in shapes)
print(f"Total area: {total_area:.2f}")
```

## Development

### Prerequisites

- Python 3.8+
- pip

### Setting Up Development Environment

1. Clone the repository:
   ```bash
   git clone https://github.com/dimarye/geometry-lib.git
   cd geometry-lib
   ```

2. Create and activate a virtual environment:
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate
   
   # Unix/macOS
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install development dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running Tests

Run all tests:
```bash
pytest tests/
```

Run tests with coverage report:
```bash
pytest --cov=geometry_lib tests/
```

### Code Style and Linting

Format code with Black:
```bash
black .
```

Sort imports with isort:
```bash
isort .
```

Run type checking:
```bash
mypy .
```

Run linter:
```bash
pylint geometry_lib/
```

### Building for Distribution

```bash
pip install build
python -m build
```

### Development Dependencies

- **Testing**: pytest, pytest-cov
- **Code Style**: black, isort
- **Type Checking**: mypy
- **Linting**: pylint
- **Documentation**: sphinx, sphinx-rtd-theme

All development dependencies are listed in `requirements.txt`.

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
