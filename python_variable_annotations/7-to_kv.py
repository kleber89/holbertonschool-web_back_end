#!/usr/bin/env python3
"""
to_kv Module
============

This module provides a function to create
a tuple where the first element is a string
and the second element is the square of a number (as a float).

Functions
---------
to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]
    Create a tuple where the first element is a string
    and the second is the square of a number.

Examples
--------
>>> from to_kv_module import to_kv
>>> to_kv("example", 3)
('example', 9.0)
>>> to_kv("data", 2.5)
('data', 6.25)
>>> to_kv("number", -4)
('number', 16.0)
"""

from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """
    Create a tuple where the first element is
    a string and the second is the square of a number.

    Parameters
    ----------
    k : str
        The string to be used as the first element of the tuple.
    v : int or float
        The number to be squared and used as the second element of the tuple.

    Returns
    -------
    tuple of (str, float)
        A tuple where the first element is the string `k`
        and the second element is the square of `v`, as a float.

    Examples
    --------
    >>> to_kv("example", 3)
    ('example', 9.0)
    >>> to_kv("data", 2.5)
    ('data', 6.25)
    >>> to_kv("number", -4)
    ('number', 16.0)
    """
    return k, float(v) ** 2
