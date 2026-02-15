"""Tests for calculator module."""

import pytest
from prueba.calculator import add, subtract, multiply, divide


class TestAdd:
    """Tests for add function."""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers."""
        assert add(2, 3) == 5
        assert add(10, 20) == 30
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        assert add(-5, -3) == -8
        assert add(-10, -15) == -25
    
    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers."""
        assert add(5, -3) == 2
        assert add(-10, 15) == 5
    
    def test_add_floats(self):
        """Test adding floating point numbers."""
        assert add(2.5, 3.5) == 6.0
        assert add(1.1, 2.2) == pytest.approx(3.3)


class TestSubtract:
    """Tests for subtract function."""
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        assert subtract(5, 3) == 2
        assert subtract(20, 10) == 10
    
    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""
        assert subtract(-5, -3) == -2
        assert subtract(-15, -10) == -5
    
    def test_subtract_mixed_numbers(self):
        """Test subtracting with mixed signs."""
        assert subtract(5, -3) == 8
        assert subtract(-10, 5) == -15
    
    def test_subtract_floats(self):
        """Test subtracting floating point numbers."""
        assert subtract(5.5, 2.5) == 3.0
        assert subtract(3.3, 1.1) == pytest.approx(2.2)


class TestMultiply:
    """Tests for multiply function."""
    
    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        assert multiply(2, 3) == 6
        assert multiply(5, 4) == 20
    
    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        assert multiply(-2, -3) == 6
        assert multiply(-5, -4) == 20
    
    def test_multiply_mixed_numbers(self):
        """Test multiplying with mixed signs."""
        assert multiply(2, -3) == -6
        assert multiply(-5, 4) == -20
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        assert multiply(5, 0) == 0
        assert multiply(0, 10) == 0
    
    def test_multiply_floats(self):
        """Test multiplying floating point numbers."""
        assert multiply(2.5, 2.0) == 5.0
        assert multiply(1.5, 2.5) == pytest.approx(3.75)


class TestDivide:
    """Tests for divide function."""
    
    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        assert divide(6, 2) == 3.0
        assert divide(20, 4) == 5.0
    
    def test_divide_negative_numbers(self):
        """Test dividing negative numbers."""
        assert divide(-6, -2) == 3.0
        assert divide(-20, -4) == 5.0
    
    def test_divide_mixed_numbers(self):
        """Test dividing with mixed signs."""
        assert divide(6, -2) == -3.0
        assert divide(-20, 4) == -5.0
    
    def test_divide_floats(self):
        """Test dividing floating point numbers."""
        assert divide(5.0, 2.0) == 2.5
        assert divide(7.5, 2.5) == pytest.approx(3.0)
    
    def test_divide_by_zero_raises_error(self):
        """Test that dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)
