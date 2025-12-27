import pandas as pd
import random

# Number of dummy records
num_students = 30

# Possible values
grades = [6, 7, 8, 9, 10]
genres = ["Fiction", "Science", "History", "Comics", "Biography"]
months = ["January", "February", "March", "April", "May", "June"]

data = []

for i in range(1, num_students + 1):
    student_id = f"S{str(i).zfill(3)}"
    grade = random.choice(grades)
    books_borrowed = random.randint(0, 10)
    reading_hours = random.randint(1, 25)
    genre = random.choice(genres)
    month = random.choice(months)

    data.append([
        student_id,
        grade,
        books_borrowed,
        reading_hours,
        genre,
        month
    ])

# Create DataFrame
df = pd.DataFrame(
    data,
    columns=[
        "Student_ID",
        "Grade",
        "Books_Borrowed",
        "Reading_Hours",
        "Genre",
        "Month"
    ]
)

# Save to CSV
df.to_csv("library_data.csv", index=False)

print("Dummy library data generated successfully!")
