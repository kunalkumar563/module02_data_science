import sqlite3
import pandas as pd

# Database connect
conn = sqlite3.connect("faculty.db")

cursor = conn.cursor()

# Create Faculty Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS faculty (
    name TEXT,
    subject TEXT,
    experience INTEGER,
    salary INTEGER
)
""")

# Delete old data
cursor.execute("DELETE FROM faculty")

# Insert Data
cursor.execute("INSERT INTO faculty VALUES ('Kunal','Python',5,0)")
cursor.execute("INSERT INTO faculty VALUES ('Monika','Data Science',8,0)")
cursor.execute("INSERT INTO faculty VALUES ('Suraj','Machine Learning',10,0)")

conn.commit()

# Create DataFrame from database
df = pd.read_sql_query("SELECT * FROM faculty", conn)

print("Original DataFrame:\n")
print(df)

# Number of students allocated
students = [40, 60, 80]

# Fee per student
fee = 500

# Salary calculation
df["students_allocated"] = students

df["salary"] = df["students_allocated"] * fee

print("\nUpdated DataFrame:\n")
print(df)

# Sort by salary in descending order
sorted_df = df.sort_values(by="salary", ascending=False)

print("\nSorted by Salary (Descending):\n")
print(sorted_df)

# Mean Salary
mean_salary = df["salary"].mean()

print("\nMean Salary:")
print(mean_salary)

# Faculty earning above mean salary
above_mean = df[df["salary"] > mean_salary]

print("\nFaculty earning above mean salary:\n")
print(above_mean)

# Close connection
conn.close()