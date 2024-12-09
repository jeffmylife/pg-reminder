import psycopg2
from psycopg2 import Error
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Load environment variables from .env file
load_dotenv()

# Database connection parameters from .env
db_params = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT")
}

# Create reminder datetime for now 
reminder_time = datetime.now() 

try:
    # Connect to the database
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Insert reminder query
    insert_query = """
    INSERT INTO reminders (reminder_text, reminder_datetime)
    VALUES (%s, %s)
    RETURNING id, reminder_datetime;
    """
    
    # Execute the query with parameters
    cursor.execute(insert_query, ("This is a test reminder!", reminder_time))
    
    # Fetch the inserted record's id and time
    reminder_id, scheduled_time = cursor.fetchone()
    
    # Commit the transaction
    connection.commit()
    
    print(f"Reminder created successfully!")
    print(f"Reminder ID: {reminder_id}")
    print(f"Scheduled for: {scheduled_time}")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL:", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection closed") 