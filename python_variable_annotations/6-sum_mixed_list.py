#!/usr/bin/env python3
"""
sum_mixed_list Module
=====================

This module provides a function to calculate
the sum of a list containing both integers and floating-point numbers.

Functions
---------
sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float
    Calculate the sum of a list containing integers and floating-point numbers.

Examples
--------
>>> from sum_mixed_list_module import sum_mixed_list
>>> sum_mixed_list([1, 2.5, 3])
6.5
>>> sum_mixed_list([0, -1.5, 2.5])
1.0
>>> sum_mixed_list([])
0.0
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list containing
    both integers and floating-point numbers.

    Parameters
    ----------
    mxd_lst : list of int and float
        A list containing integers and floating-point numbers to be summed.

    Returns
    -------
    float
        The sum of all numbers in the input list as a floating-point number.

    Examples
    --------
    >>> sum_mixed_list([1, 2.5, 3])
    6.5
    >>> sum_mixed_list([0, -1.5, 2.5])
    1.0
    >>> sum_mixed_list([])
    0.0
    """
    return float(sum(mxd_lst))
