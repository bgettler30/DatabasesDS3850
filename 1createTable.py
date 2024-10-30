import sqlite3

# Step 1: Connect to the database (or create it if it doesn't exist)
connection = sqlite3.connect('DatabaseFile.db')  # This creates a new database file if not existing.

# Step 2: Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Step 3: Create the StudentInfo table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS StudentInfo (
        StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName TEXT NOT NULL,
        LastName TEXT NOT NULL
    )
''')

print("StudentInfo table created successfully.")

# Step 4: Commit the changes and close the connection
connection.commit()
connection.close()

