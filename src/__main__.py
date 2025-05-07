#!/usr/bin/env python3
"""
Main entry point for the python-classroom-template package.

This allows running the package directly with:
python -m src
"""

from src.example import add, subtract


def main() -> None:
    """Run a simple demonstration of the package functionality."""
    print("Python Classroom Template - Example")
    print("-" * 40)
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print("-" * 40)
    print("Edit __main__.py to customize this demo")


if __name__ == "__main__":
    main()