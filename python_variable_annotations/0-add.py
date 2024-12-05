#!/usr/bin/env python3
"""
Module 0-add.py
==========

This module provides a simple function to add two floating-point numbers.

Functions
---------
add(a: float, b: float) -> float
    Add two floating-point numbers and return their sum.

Examples
--------
>>> from add_module import add
>>> add(3.5, 2.5)
6.0
>>> add(-1.0, 4.0)
3.0
"""


def add(a: float, b: float) -> float:
    """
    Add two floating-point numbers and return their sum.

    Parameters
    ----------
    a : float
        The first number to add.
    b : float
        The second number to add.

    Returns
    -------
    float
        The sum of `a` and `b`.

    Examples
    --------
    >>> add(3.5, 2.5)
    6.0
    >>> add(-1.0, 4.0)
    3.0
    """
    return a + b
