import sqlite3
import pandas as pd
import random

# Database connect
conn = sqlite3.connect("students.db")

cursor = conn.cursor()
# Delete old table
cursor.execute("DROP TABLE IF EXISTS students")

# Create new table
cursor.execute("""
CREATE TABLE students (
    name TEXT,
    subject TEXT,
    enroll_no INTEGER,
    cgpa REAL,
    email TEXT
)
""")

# Sample Data
names = [
    "Kunal", "Monika", "Krish", "Suraj", "Sunny",
    "Moni", "Tulaj", "Monu", "Don", "Aman"
]

subjects = [
    "Python",
    "Data Science",
    "Machine Learning",
    "Java",
    "Web Development"
]

# Insert 100 rows
for i in range(1, 101):

    name = random.choice(names)

    subject = random.choice(subjects)

    enroll_no = 1000 + i

    cgpa = round(random.uniform(6.0, 9.8), 2)

    email = name.lower() + str(i) + "@gmail.com"

    cursor.execute("""
    INSERT INTO students
    VALUES (?, ?, ?, ?, ?)
    """, (name, subject, enroll_no, cgpa, email))

# Save changes
conn.commit()

# Database -> DataFrame
df = pd.read_sql_query("SELECT * FROM students", conn)

# Display first 10 rows
print(df.head(10))

# Close connection
conn.close()