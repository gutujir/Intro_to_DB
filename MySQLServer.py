#!/usr/bin/python3
"""Script to create the alx_book_store database in MySQL"""

import MySQLdb
from sys import argv


def create_database():
    """Creates the alx_book_store database"""
    try:
        # Connect to MySQL server (without specifying a database)
        db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            port=3306
        )

        # Create cursor object
        cursor = db.cursor()

        # Create database (IF NOT EXISTS prevents failure if DB already exists)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        # Close database connection
        if 'db' in locals() and db.open:
            db.close()


if __name__ == "__main__":
    if len(argv) != 3:
        print("Usage: python MySQLServer.py <username> <password>")
    else:
        create_database()
