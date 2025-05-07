"""
Tests for the Introduction to Variables exercises.

These tests verify that the variable functions are implemented correctly.
"""

import pytest
from src.topics.intro_to_variables.variables import (
    create_variable,
    create_string_variable,
    add_variables,
    concatenate_strings,
    variable_type_conversion
)


def test_create_variable() -> None:
    """Test that create_variable returns the integer value 42."""
    result = create_variable()
    assert isinstance(result, int), "The result should be an integer"
    assert result == 42, "The result should be 42"


def test_create_string_variable() -> None:
    """Test that create_string_variable returns the string 'Hello, Python!'."""
    result = create_string_variable()
    assert isinstance(result, str), "The result should be a string"
    assert result == "Hello, Python!", "The result should be 'Hello, Python!'"


def test_add_variables() -> None:
    """Test that add_variables correctly adds two integers."""
    test_cases = [
        (5, 7, 12),
        (0, 0, 0),
        (-3, 3, 0),
        (100, 42, 142)
    ]
    
    for a, b, expected in test_cases:
        result = add_variables(a, b)
        assert isinstance(result, int), f"The result of adding {a} and {b} should be an integer"
        assert result == expected, f"The result of adding {a} and {b} should be {expected}"


def test_concatenate_strings() -> None:
    """Test that concatenate_strings correctly joins two strings."""
    test_cases = [
        ("Hello", " World", "Hello World"),
        ("Python", " is fun", "Python is fun"),
        ("", "Empty", "Empty"),
        ("Combine ", "strings", "Combine strings")
    ]
    
    for str1, str2, expected in test_cases:
        result = concatenate_strings(str1, str2)
        assert isinstance(result, str), f"The result of concatenating '{str1}' and '{str2}' should be a string"
        assert result == expected, f"The result of concatenating '{str1}' and '{str2}' should be '{expected}'"


def test_variable_type_conversion() -> None:
    """Test that variable_type_conversion correctly converts strings to integers."""
    test_cases = [
        ("10", 10),
        ("0", 0),
        ("-5", -5),
        ("42", 42),
        ("100", 100)
    ]
    
    for num_str, expected in test_cases:
        result = variable_type_conversion(num_str)
        assert isinstance(result, int), f"The result of converting '{num_str}' should be an integer"
        assert result == expected, f"The result of converting '{num_str}' should be {expected}"