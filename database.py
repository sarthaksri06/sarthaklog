import sqlite3
from werkzeug.security import generate_password_hash
import os

DATABASE_PATH = 'users.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized successfully")

def create_user(fullname, email, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    hashed_password = generate_password_hash(password)
    
    try:
        cursor.execute(
            'INSERT INTO users (fullname, email, password) VALUES (?, ?, ?)',
            (fullname, email, hashed_password)
        )
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()
        return user_id
    except sqlite3.IntegrityError:
        conn.close()
        return None

def get_user_by_email(email):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
    user = cursor.fetchone()
    
    conn.close()
    return user

def get_user_by_id(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    
    conn.close()
    return user

def get_all_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT id, fullname, email, created_at FROM users')
    users = cursor.fetchall()
    
    conn.close()
    return users

def update_user_password(email, new_password):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    hashed_password = generate_password_hash(new_password)
    
    cursor.execute(
        'UPDATE users SET password = ? WHERE email = ?',
        (hashed_password, email)
    )
    conn.commit()
    affected_rows = cursor.rowcount
    conn.close()
    
    return affected_rows > 0

def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    affected_rows = cursor.rowcount
    conn.close()
    
    return affected_rows > 0