import mysql.connector


def connect():
# Initialize a variable to hold the database connection
    conn = None

    try:
        # Attempt to establish a connection to the MySQL database
        conn = mysql.connector.connect(host='localhost', port=3307,database='creditcard_vault', user='root',password='')
        
        # Check if the connection is successfully established
        if conn.is_connected():
            print('Connected to MySQL database')

    except mysql.connector.Error as e:
        # Print an error message if a connection error occurs
        print(e)

    finally:
        # Close the database connection in the 'finally' block to ensure it happens
        if conn is not None and conn.is_connected():
            conn.close()