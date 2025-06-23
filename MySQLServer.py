import mysql.connector
from mysql.connector import Error

DB_NAME = 'alx_book_store'

try:
    # Connect to MySQL server (adjust user and password as needed)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',  # Change if your MySQL user is different
        password=''   # Add your MySQL password if needed
    )
    if connection.is_connected():
        cursor = connection.cursor()
        try:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print(f"Database '{DB_NAME}' created successfully!")
        except Error as e:
            print(f"Error creating database: {e}")
        finally:
            cursor.close()
    else:
        print("Failed to connect to MySQL server.")
except Error as e:
    print(f"Error connecting to MySQL: {e}")
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
