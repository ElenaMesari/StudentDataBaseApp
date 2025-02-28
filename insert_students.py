import sqlite3

 
conn = sqlite3.connect('students.db')
cursor = conn.cursor()
 
students = [
    ("Alice", 14, "A"),
    ("Bob", 15, "B"),
    ("Charlie", 13, "A"),
    ("David", 16, "C"),
    ("Emma", 14, "B")
]

 
cursor.executemany("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", students)

 
conn.commit()
conn.close()

print("Sample students added successfully!")
