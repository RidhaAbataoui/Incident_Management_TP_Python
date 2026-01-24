import sqlite3
import os

DB_PATH = "data/incident.db"

def init_database():
    os.makedirs("data",exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT CHECK(role IN ('admin', 'employee')) NOT NULL
        );
        """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT DEFAULT 'OPEN',
            user_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id)
        );
        """)

    cursor.execute("""
    INSERT OR IGNORE INTO users (id, name, email, password, role)
    VALUES (1, 'Admin', 'admin@system.com', 'admin123', 'admin')
    """)

    conn.commit()
    conn.close()
    print("Database initialized successfully")

if __name__ == "__main__":
    init_database()