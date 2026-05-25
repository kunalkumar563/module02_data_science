import pandas as pd

# Data
data = {
    "Name": ["Kunal", "Monika", "Krish", "Suraj"],
    "Age": [12 , 21, 21, 20],
    "Marks": [45, 90, 99, 88],
    "grade": ["C", "A+", "A++", "A"]
}

# DataFrame create
df = pd.DataFrame(data)

# Excel file create
df.to_excel("students.xlsx", index=False)

print("Excel File Created Successfully!")