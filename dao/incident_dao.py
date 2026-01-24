from dao.database import get_connection

def create_incident(title, description,user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO incidents (title, description, user_id) VALUES (?, ?, ?)",
        (title, description, user_id)
    )
    conn.commit()
    conn.close()

def get_incident_by_id(incident_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM incidents WHERE id = ?", (incident_id,))
    incident = cur.fetchone()
    conn.close()
    return incident

def get_incidents_by_user(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM incidents WHERE user_id = ?",
        (user_id,)
    )
    rows = cur.fetchall()
    conn.close()
    return rows

def get_all_incidents():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM incidents")
    rows = cur.fetchall()
    conn.close()
    return rows

def update_incident_status(incident_id, status):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE incidents SET status = ? WHERE id = ?
        """,(status, incident_id)
    )
    conn.commit()
    conn.close()

def delete_incident(incident_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM incidents WHERE id = ?", (incident_id,))
    conn.commit()
    conn.close()