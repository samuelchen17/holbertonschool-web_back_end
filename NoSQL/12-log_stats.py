#!/usr/bin/env python3
"""This module displays stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient


def main():
    """display Nginx log stats"""
    # default port
    client = MongoClient("mongodb://localhost:27017")

    collection = client.logs.nginx

    print(f"{collection.count_documents({})} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_count = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print("{} status check".format(status_count))


if __name__ == "__main__":
    main()
