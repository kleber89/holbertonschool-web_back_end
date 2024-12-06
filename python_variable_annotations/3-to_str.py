#!/usr/bin/env python3
"""
Module 3-to_str.py
=============

This module provides a function to convert
a floating-point number into its string representation.

Functions
---------
to_str(n: float) -> str
    Convert a floating-point number to its string representation.

Examples
--------
>>> from to_str_module import to_str
>>> to_str(3.14)
'3.14'
>>> to_str(-0.001)
'-0.001'
>>> to_str(0.0)
'0.0'
"""


def to_str(n: float) -> str:
    """
    Convert a floating-point number to its string representation.

    Parameters
    ----------
    n : float
        The floating-point number to convert.

    Returns
    -------
    str
        The string representation of the input float.

    Examples
    --------
    >>> to_str(3.14)
    '3.14'
    >>> to_str(-0.001)
    '-0.001'
    >>> to_str(0.0)
    '0.0'
    """
    return str(n)
