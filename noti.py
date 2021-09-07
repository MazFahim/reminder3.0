from plyer import notification
import sqlite3
import datetime
import time


def no(priority, title, details, d, m, h):
    current_time = datetime.datetime.now()
    month = current_time.strftime("%m")
    day = current_time.strftime("%d")
    hour = current_time.strftime("%H")
    print(month)
    if int(month) == m:
        print("M")
        if int(day) == d:
            print("D")
            if int(hour) == h:
                print("H")
                notification.notify(
                    title=title,
                    message="Priority-" + str(priority) + ", " + details,
                    app_icon=None,
                    timeout='10'
                )
    time.sleep(60)


try:
    conn = sqlite3.connect('reminder3.db')
    cursor = conn.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute("SELECT * FROM tasks")

    rows = cursor.fetchall()
    print("ID--Priority--Title--Details--Day--Month--Hour")
    for row in rows:
        no(row[1], row[2], row[3], row[4], row[5], row[6])
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)
