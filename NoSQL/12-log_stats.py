#!/usr/bin/env python3
"""
Log stats.

This script connects to a MongoDB instance and retrieves statistics about Nginx logs stored in a collection.
It provides an overview of the total log count, the number of logs for different HTTP methods, and the count of status check requests.
"""

from pymongo import MongoClient


def logs_stats(numbers):
    client = MongoClient('mongodb://localhost:27017/')  # Adjust the connection string if needed
    logs = client.logs.nginx
    return logs.count_documents(numbers)

def main():
    """
    Main function to connect to MongoDB, retrieve Nginx log statistics,
    and print the results in a specified format.
    """
    
    # Define the HTTP methods to count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    # Display results
    print(f"{logs_stats({})} logs")  # Print total number of logs
    print("Methods:")  # Print header for methods
    for method in methods:
        print(f"\tmethod {method}: {logs_stats({'method': method})}")
    print(f"{logs_stats({'method': 'GET', 'path': '/status'})} status check")
    

if __name__ == "__main__":
    main()  # Execute the main function