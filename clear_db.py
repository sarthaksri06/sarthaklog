import sqlite3
import os

def delete_all_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM users")
    conn.commit()
    
    print(f"Deleted {cursor.rowcount} users from database")
    conn.close()

# Or completely delete the database file
def delete_database():
    if os.path.exists('users.db'):
        os.remove('users.db')
        print("Database file deleted")
    else:
        print("Database file not found")

# Choose one:
delete_all_users()  # Keeps table structure, removes all users
# delete_database()  # Deletes entire database file
