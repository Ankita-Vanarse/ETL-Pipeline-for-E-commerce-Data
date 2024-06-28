import boto3
import pandas as pd
from io import StringIO
import mysql.connector

def lambda_handler(event, context):
    # Process the CSV content
    df = pd.read_csv('Departments.csv')


    # Database connection setup
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '1234',
        'database': 'ecom_schema'
    }

    # Establish the connection
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Insert data into MySQL
    table_name = 'Departments'

    # Create a list of tuples from the DataFrame values
    data = [tuple(row) for row in df.values]

    # Generate the column names from the DataFrame
    columns = ", ".join(df.columns)

    # Generate the placeholder string (e.g., "%s, %s, %s")
    placeholders = ", ".join(["%s"] * len(df.columns))

    # Create the SQL insert statement with ON DUPLICATE KEY UPDATE
    insert_stmt = f"""
    INSERT INTO {table_name} ({columns})
    VALUES ({placeholders})
    ON DUPLICATE KEY UPDATE
    {', '.join([f'{col}=VALUES({col})' for col in df.columns if col != 'DepartmentID'])}
    """

    # Execute the insert statement
    cursor.executemany(insert_stmt, data)

    # Commit the transaction
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    print("Data inserted successfully")
    print('All done')

    return {
        'statusCode': 200,
        'body': 'CSV processed successfully'
    }

lambda_handler("", "")
