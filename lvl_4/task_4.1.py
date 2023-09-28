# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:


import sqlite3

# Создание базы данных
conn = sqlite3.connect('teacher.db')
cursor = conn.cursor()

# Создание таблицы Students
cursor.execute('CREATE TABLE Students (Student_Id INTEGER, Student_Name TEXT, School_Id INTEGER PRIMARY KEY)')

# Наполнение таблицы данными
students = [
    (201, 'Иван', 1),
    (202, 'Петр', 2),
    (203, 'Анастасия', 3),
    (204, 'Игорь', 4)
]
cursor.executemany('INSERT INTO Students VALUES (?, ?, ?)', students)

# Функция для получения информации о школе и студенте по ID
def get_info(student_id):
    cursor.execute('SELECT * FROM Students WHERE Student_Id = ?', (student_id,))
    student = cursor.fetchone()
    
    if student:
        school_id = student[2]
        cursor.execute('SELECT * FROM Schools WHERE School_Id = ?', (school_id,))
        school = cursor.fetchone()
        
        if school:
            return f'ID Студента: {student[0]}\nИмя студента: {student[1]}\nID школы: {school[0]}\nНазвание школы: {school[1]}'
        else:
            return 'Школа не найдена'
    else:
        return 'Студент не найден'

# Создание таблицы Schools
cursor.execute('CREATE TABLE Schools (School_Id INTEGER PRIMARY KEY, School_Name TEXT)')

# Наполнение таблицы данными
schools = [
    (1, 'Школа №1'),
    (2, 'Школа №2'),
    (3, 'Школа №3'),
    (4, 'Школа №4')
]
cursor.executemany('INSERT INTO Schools VALUES (?, ?)', schools)

conn.commit()
conn.close()

# Пример использования функции
student_id = 201
print(get_info(student_id))