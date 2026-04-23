import sqlite3

def connect():
    conn = sqlite3.connect("students.db")
    return conn

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll_number TEXT NOT NULL UNIQUE,
            maths INTEGER NOT NULL,
            science INTEGER NOT NULL,
            english INTEGER NOT NULL,
            percentage REAL NOT NULL,
            grade TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"

def calculate_status(percentage):
    if percentage >= 40:
        return "Pass"
    else:
        return "Fail"

def add_student(name, roll_number, maths, science, english):
    percentage = round((maths + science + english) / 3, 2)
    grade = calculate_grade(percentage)
    status = calculate_status(percentage)
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO students 
        (name, roll_number, maths, science, english, percentage, grade, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, roll_number, maths, science, english, percentage, grade, status))
    conn.commit()
    conn.close()

def get_all_students():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return students

def delete_student(id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update_student(id, name, roll_number, maths, science, english):
    percentage = round((maths + science + english) / 3, 2)
    grade = calculate_grade(percentage)
    status = calculate_status(percentage)
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE students
        SET name=?, roll_number=?, maths=?, science=?, 
            english=?, percentage=?, grade=?, status=?
        WHERE id=?
    ''', (name, roll_number, maths, science, english, 
          percentage, grade, status, id))
    conn.commit()
    conn.close()

def search_student(keyword):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM students
        WHERE name LIKE ? OR roll_number LIKE ?
    ''', (f"%{keyword}%", f"%{keyword}%"))
    students = cursor.fetchall()
    conn.close()
    return students

def get_toppers():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM students 
        ORDER BY percentage DESC LIMIT 3
    ''')
    students = cursor.fetchall()
    conn.close()
    return students

create_table()
