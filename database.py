import sqlite3
import pandas as pd

# Database connect
conn = sqlite3.connect("students.db")

# Create table
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER,
    name TEXT,
    age INTEGER,
    marks INTEGER
)
""")

# Insert data
cursor.execute("INSERT INTO students VALUES (1,'Kunal',20,85)")
cursor.execute("INSERT INTO students VALUES (2,'Monika',21,90)")
cursor.execute("INSERT INTO students VALUES (3,'Krish',19,76)")
cursor.execute("INSERT INTO students VALUES (4,'Suraj',22,65)")
cursor.execute("INSERT INTO students VALUES (5,'Sunny',23,88)")

conn.commit()

# Database se DataFrame banana
df = pd.read_sql_query("SELECT * FROM students", conn)

print("Original DataFrame:\n")
print(df)

# Ascending sort using Age
ascending_df = df.sort_values(by="age", ascending=True)

print("\nAscending Order:\n")
print(ascending_df)

# Descending sort using Age
descending_df = df.sort_values(by="age", ascending=False)

print("\nDescending Order:\n")
print(descending_df)

# Mean of marks
mean_marks = df["marks"].mean()

print("\nMean of Marks:")
print(mean_marks)

# Students having marks greater than mean
above_mean = df[df["marks"] > mean_marks]

print("\nStudents scoring above mean:\n")
print(above_mean)

# Connection close
conn.close()