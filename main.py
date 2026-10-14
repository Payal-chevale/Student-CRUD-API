

from fastapi import FastAPI
import sqlite3

app = FastAPI()

# Database connection and table creation
def create_table():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            age INTEGER NOT NULL,
            course TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

create_table()


@app.get("/")
def home():
    return {"message": "Student CRUD API is running!"}


@app.get("/students")
def get_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    conn.close()

    return {"students": rows}

from pydantic import BaseModel, EmailStr

class Student(BaseModel):
    name: str
    email: EmailStr
    age: int
    course: str


@app.post("/students")
def create_student(student: Student):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO students (name, email, age, course)
        VALUES (?, ?, ?, ?)
        """,
        (student.name, student.email, student.age, student.course)
    )

    conn.commit()
    student_id = cursor.lastrowid
    conn.close()

    return {
        "message": "Student created successfully",
        "student_id": student_id,
        "name": student.name
    }

@app.get("/students/{student_id}")
def get_student(student_id: int):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()
    conn.close()

    if student is None:
        return {"message": "Student not found"}

    return {
        "id": student[0],
        "name": student[1],
        "email": student[2],
        "age": student[3],
        "course": student[4]
    }

from fastapi import HTTPException


@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE students
        SET name = ?, email = ?, age = ?, course = ?
        WHERE id = ?
        """,
        (
            student.name,
            student.email,
            student.age,
            student.course,
            student_id
        )
    )

    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    conn.commit()
    conn.close()

    return {
        "message": "Student updated successfully",
        "student_id": student_id
    }

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    conn.commit()
    conn.close()

    return {
        "message": "Student deleted successfully",
        "student_id": student_id
    }
