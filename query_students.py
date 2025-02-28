import sqlite3
import pandas as pd
 
conn = sqlite3.connect('students.db')

 
df = pd.read_sql("SELECT * FROM students ORDER BY grade ASC", conn)

 
conn.close()

 
print(df)
