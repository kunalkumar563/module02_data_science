import pandas as pd

# Create DataFrame
data = {
    "Name": [
        "Kunal", "monika", "sunny", "suraj", "moni",
        "momo", "krishna", "krish", "monu", "gudlahi"
    ],
    
    "Age": [20, 22, 19, 21, 23, 24, 20, 22, 21, 25],
    
    "Marks": [85, 72, 90, 65, 88, 70, 95, 60, 78, 82]
}

df = pd.DataFrame(data)

# Display DataFrame
print("Original DataFrame:\n")
print(df)

# Mean of marks
mean_marks = df["Marks"].mean()
print("\nMean of Marks:")
print(mean_marks)

# Lowest 5 members based on marks
lowest_5 = df.nsmallest(5, "Marks")

print("\nLowest 5 Members:")
print(lowest_5)

# Sort DataFrame based on Age
sorted_df = df.sort_values(by="Age")

print("\nDataFrame Sorted by Age:")
print(sorted_df)