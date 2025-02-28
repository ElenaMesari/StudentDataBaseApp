import streamlit as st
import pandas as pd
import sqlite3


def load_students():
    conn = sqlite3.connect('students.db')
    df = pd.read_sql("SELECT * FROM students ORDER BY grade ASC", conn)
    conn.close()
    return df

 
def add_student(name, age, grade):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
                   (name, age, grade))
    conn.commit()
    conn.close()


def delete_student(student_id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    conn.close()

 
def update_grade(student_id, new_grade):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET grade=? WHERE id=?", (new_grade, student_id))
    conn.commit()
    conn.close()


st.title("📚 Student Database")

st.subheader("Add a New Student")
with st.form("student_form"):
    name = st.text_input("Student Name")
    age = st.number_input("Age", min_value=5, max_value=100, step=1)
    grade = st.selectbox("Grade", ["A", "B", "C", "D", "F"])
    submitted = st.form_submit_button("Add Student")

    if submitted:
        add_student(name, age, grade)
        st.success("Student added successfully!")

 
st.subheader("Student List")
df_students = load_students()

if not df_students.empty:
    st.dataframe(df_students)

     
    student_id = st.number_input("Enter Student ID to Update Grade", min_value=1, step=1)
    new_grade = st.selectbox("New Grade", ["A", "B", "C", "D", "F"])
    if st.button("Update Grade"):
        update_grade(student_id, new_grade)
        st.success("Grade updated! Refresh the page to see changes.")

    
    delete_id = st.number_input("Enter Student ID to Delete", min_value=1, step=1)
    if st.button("Delete Student"):
        delete_student(delete_id)
        st.warning("Student deleted! Refresh the page to see changes.")

else:
    st.write("No students found.")

