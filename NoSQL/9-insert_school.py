#!/usr/bin/env python3
"""Python function that inserts a new document"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into the specified MongoDB collection.

    Parameters:
    mongo_collection: The pymongo collection object where the document will be inserted.
    **kwargs: The fields and values to be included in the new document.

    Returns:
    The new document's _id.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id