#!/usr/bin/env python3
"""
Module 2-floor.py
============

This module provides a function to compute the floor of a floating-point number.

Functions
---------
floor(n: float) -> int
    Return the floor of a floating-point number.

Examples
--------
>>> from floor_module import floor
>>> floor(3.7)
3
>>> floor(-2.3)
-3
>>> floor(0.0)
0
"""


import math


def floor(n: float) -> int:
    """
    Return the floor of a floating-point number.

    The floor of a number is the largest integer less than or equal to the number.

    Parameters
    ----------
    n : float
        The floating-point number to calculate the floor of.

    Returns
    -------
    int
        The floor of the input number as an integer.

    Examples
    --------
    >>> floor(3.7)
    3
    >>> floor(-2.3)
    -3
    >>> floor(0.0)
    0
    """
    return math.floor(n)
