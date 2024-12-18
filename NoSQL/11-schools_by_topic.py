#!/usr/bin/env python3
"""11. Where can I learn Python?"""

def schools_by_topic(mongo_collection, topic):
    """Returns a list of all documents in the
    collection where the topic is present in the dictionary of"""
    return mongo_collection.find({"topics": topic})