from dao.database import get_connection

def create_user(name,email,password,role):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)",
        (name, email, password, role)
    )
    conn.commit()
    user_id = cur.lastrowid
    conn.close()
    return user_id

def get_user_all_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email, role FROM users")
    user = cur.fetchall()
    conn.close()
    return user

def get_user_by_email(email):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cur.fetchone()
    conn.close()
    return user

def update_user(user_id,name,email,role):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    UPDATE users SET name = ?, email = ?, role = ? WHERE id = ?
    """,(name, email, role, user_id))
    conn.commit()
    conn.close()

def delete_user(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()