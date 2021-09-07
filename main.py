# bismillahir rahmanir rahim

import sqlite3


def db_insert(pri, title, details, date, month, hour):
    cursor.execute("""INSERT INTO tasks
                              (priority, Title, Details, Date, Month, Hour) 
                               VALUES 
                              (?,?,?,?,?,?)""", (pri, title, details, date, month, hour))
    conn.commit()
    print("Record inserted successfully into tasks table ", cursor.rowcount)
    cursor.execute("SELECT * FROM tasks")

    rows = cursor.fetchall()
    print("ID--Priority--Title--Details--Day--Month--Hour")
    for row in rows:
        print(row)
    cursor.close()


def show_all():
    cursor.execute("SELECT * FROM tasks")

    rows = cursor.fetchall()
    print("ID--Priority--Title--Details--Day--Month--Hour")
    for row in rows:
        print(row)
    cursor.close()


try:
    conn = sqlite3.connect('reminder3.db')
    cursor = conn.cursor()
    print("Successfully Connected to SQLite")

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)

priority_list = {"Lab Report": 1,
                 "Exam": 1,
                 "Project": 2,
                 "Tuition": 3,
                 "Study": 4,
                 "Others": 5}

while True:
    option = int(input("Enter 1 to set new reminder, 2 to see all the reminder,3 to delete a reminder and 4 to exit:"))
    if option == 1:
        priority = int(input("Enter the priority level from 1-5:"))
        task_title = input("Title of the reminder:")
        task_details = input("Details of the reminder:")
        task_date = int(input("Date of the reminder:"))
        task_month = int(input("Month of the reminder:"))
        task_hour = int(input("Hour of the reminder:"))

        print(priority, task_title, task_details, task_date, task_month, task_hour)
        db_insert(priority, task_title, task_details, task_date, task_month, task_hour)
    elif option == 2:
        show_all()
    elif option == 3:
        print("Delete option hasn't been set up")
    elif option==4:
        print("Job done")
        break

