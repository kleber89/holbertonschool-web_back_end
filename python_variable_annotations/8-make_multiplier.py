#!/usr/bin/env python3
"""
make_multiplier Module
======================

This module provides a function to create a multiplier function.
The multiplier function takes a float as input
and returns the product of the input and a predefined multiplier.

Functions
---------
make_multiplier(multiplier: float) -> Callable[[float], float]
    Create a function that multiplies a float by a given multiplier.

Examples
--------
>>> from make_multiplier_module import make_multiplier
>>> multiplier_func = make_multiplier(3.0)
>>> multiplier_func(2.0)
6.0
>>> multiplier_func(0.5)
1.5
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a given multiplier.

    Parameters
    ----------
    multiplier : float
        The value to multiply input numbers by.

    Returns
    -------
    Callable[[float], float]
        A function that takes a float and
        returns the product of the input and the multiplier.

    Examples
    --------
    >>> multiplier_func = make_multiplier(3.0)
    >>> multiplier_func(2.0)
    6.0
    >>> multiplier_func(0.5)
    1.5
    """

    def multiply(value: float) -> float:
        return value * multiplier

    return multiply
