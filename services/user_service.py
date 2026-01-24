from dao.user_dao import *
from services.xml_export_service import *

def list_users(current_user):
    if current_user["role"] != "admin":
        raise PermissionError("You are not allowed to list users")
    return get_user_all_users()

def add_user(current_user,name,email,password,role):
    if current_user["role"] != "admin":
        raise PermissionError("You are not allowed to add user")
    create_user(name,email,password,role)
    export_users_to_xml()
    add_dtd_to_incidents_xml()


def edit_user(current_user,user_id,role):
    if current_user["role"] != "admin":
        raise PermissionError("You are not allowed to edit user")
    update_user(user_id,role)
    export_users_to_xml()
    add_users_dtd_and_xsl()

def remove_user(current_user,user_id):
    if current_user["role"] != "admin":
        raise PermissionError("You are not allowed to remove user")
    delete_user(user_id)
    export_users_to_xml()
    add_users_dtd_and_xsl()