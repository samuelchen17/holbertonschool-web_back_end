#!/usr/bin/env python3
"""Module for inserting new doc in a collection"""


def insert_school(mongo_collection, **kwargs):
    """insert new doc into collection"""
    return list(mongo_collection.find())
