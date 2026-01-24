from dao.incident_dao import *

VALID_STATUS = ("OPEN","IN_PROGRESS","RESOLVED","CLOSED")

def add_incident(title,description,user):
    return create_incident(title, description, user["id"])

def list_incidents(user):
    if user["role"]=="admin":
        return get_all_incidents()
    else:
        return get_incidents_by_user(user["id"])


def change_incident_status(current_user,incident_id,status):
    incident = get_incident_by_id(incident_id)
    if not incident:
        raise ValueError("Incident not found")
    if current_user["role"]!="admin":
        raise PermissionError("You are not allowed to change incident status")
    if status not in VALID_STATUS:
        raise PermissionError(f"Invalid status. Allowed: {VALID_STATUS}")
    return  update_incident_status(incident_id,status)

def remove_incident(current_user,incident_id):
    incident = get_incident_by_id(incident_id)
    if not incident:
        raise ValueError("Incident not found")
    if current_user["role"]!="admin":
        raise PermissionError("You are not allowed to remove incident status")
    return delete_incident(incident_id)