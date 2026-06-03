import sqlite3
import os

if os.path.exists('users.db'):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, fullname, email FROM users")
    rows = cursor.fetchall()
    print("Users in database:")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")
    conn.close()
else:
    print("users.db file not found - SQLite not being used yet")
