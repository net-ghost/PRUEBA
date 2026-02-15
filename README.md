# PRUEBA

A simple Python project demonstrating testing framework implementation with pytest.

## Features

- Simple calculator module with basic arithmetic operations
- Comprehensive test suite using pytest
- Type hints for better code quality
- Test coverage reporting

## Installation

```bash
# Install the package in development mode
pip install -e .

# Install with development dependencies
pip install -e ".[dev]"

# Or install just the test dependencies
pip install -r requirements.txt
```

## Usage

```python
from prueba.calculator import add, subtract, multiply, divide

# Basic arithmetic operations
result = add(5, 3)        # 8
result = subtract(10, 4)  # 6
result = multiply(3, 4)   # 12
result = divide(15, 3)    # 5.0
```

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=prueba --cov-report=term-missing

# Run specific test file
pytest tests/test_calculator.py

# Run specific test class
pytest tests/test_calculator.py::TestAdd

# Run specific test method
pytest tests/test_calculator.py::TestAdd::test_add_positive_numbers
```

## Project Structure

```
PRUEBA/
├── src/
│   └── prueba/
│       ├── __init__.py
│       └── calculator.py
├── tests/
│   ├── __init__.py
│   └── test_calculator.py
├── setup.py
├── requirements.txt
├── pytest.ini
└── README.md
```

## Development

This project uses:
- **pytest** for testing
- **pytest-cov** for coverage reporting
- Type hints for better code documentation

## License

This is a demonstration project.