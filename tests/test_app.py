"""This module contains tests for Projectsite"""

from app import hello_world


def test_hello_world() -> None:
    expected_value = "Hello, World did you know"
    assert hello_world().startswith(expected_value)