import mysql.connector
from mysql.connector import Error

def connect_to_server():
    try:
        # Establishing a connection to the MySQL server
        connection = mysql.connector.connect(
            host="localhost",  # Hostname of the MySQL server
            user="root",       # Username for authentication
            passwd="",         # Password for authentication
            database=""        # Note: No database specified here
        )
        
        if connection.is_connected():
            print("Connected to MySQL server")
            return connection
        
    except Error as e:
        print(f"Error connecting to MySQL server: {e}")
        return None

def create_database_and_table():
    connection = connect_to_server()
    if connection is not None:
        try:
            cursor = connection.cursor()
            
            # Create the database
            cursor.execute("CREATE DATABASE IF NOT EXISTS project_quiz")
            print("Database 'project_quiz' created successfully")

            # Switch to the database
            cursor.execute("USE project_quiz")

            # Create the signup table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS signup (
                    ID INT AUTO_INCREMENT PRIMARY KEY,
                    Name VARCHAR(255) NOT NULL,
                    Age INT NOT NULL,
                    Email VARCHAR(255) NOT NULL,
                    Phone_Number VARCHAR(20) NOT NULL,
                    Username VARCHAR(50) NOT NULL,
                    Password VARCHAR(50) NOT NULL
                )
            ''')
            print("Table 'signup' created successfully")

            # Committing the changes
            connection.commit()

        except Error as e:
            print(f"Error creating database/table: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection closed")

# Call the function to create the database and table
create_database_and_table()
