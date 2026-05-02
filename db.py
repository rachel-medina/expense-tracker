import sqlite3

DB_NAME = "expenses.db"

def connect():
    return sqlite3.connect(DB_NAME) #opens connection

def create_table():
    conn = connect() 
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT,
            amount REAL,
            category TEXT,
            date TEXT
        )
    """)

    conn.commit()
    conn.close()
