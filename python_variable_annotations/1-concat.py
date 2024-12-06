#!/usr/bin/env python3
"""
Module 1-concat.py
=============

This module provides a function to concatenate two strings.

Functions
---------
concat(str1: str, str2: str) -> str
    Concatenate two strings and return the result.

Examples
--------
>>> from concat_module import concat
>>> concat("Hello, ", "World!")
'Hello, World!'
>>> concat("Python ", "Rocks")
'Python Rocks'
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenate two strings into a single string.

    Parameters
    ----------
    str1 : str
        The first string to be concatenated.
    str2 : str
        The second string to be concatenated.

    Returns
    -------
    str
        A new string that is the result of joining str1 and str2.

    Examples
    --------
    >>> concat("Hello", " World")
    'Hello World'
    >>> concat("Python", "Docstring")
    'PythonDocstring'

    Notes
    -----
    This function uses the standard string concatenation operator (+).
    """
    return str1 + str2
