#!/usr/bin/env python3
from typing import List

"""
Module 5-sum_list.py
===============

This module provides a function to calculate the sum of a list of floating-point numbers.

Functions
---------
sum_list(input_list: List[float]) -> float
    Calculate the sum of a list of floating-point numbers.

Examples
--------
>>> from sum_list_module import sum_list
>>> sum_list([1.2, 2.3, 3.4])
6.9
>>> sum_list([-1.0, 0.0, 1.0])
0.0
>>> sum_list([])
0.0
"""


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floating-point numbers.

    Parameters
    ----------
    input_list : list of float
        A list of floating-point numbers to be summed.

    Returns
    -------
    float
        The sum of all numbers in the input list.

    Examples
    --------
    >>> sum_list([1.2, 2.3, 3.4])
    6.9
    >>> sum_list([-1.0, 0.0, 1.0])
    0.0
    >>> sum_list([])
    0.0
    """
    return sum(input_list)
