from dao.user_dao import *

def list_users(current_user):
    if current_user["role"] != "admin":
        raise PermissionError("You are not allowed to list users")
    return get_user_all_users()

def add_user(current_user,name,email,password,role):
    if current_user["role"] != "admin":
        raise PermissionError("You are not allowed to add user")
    return create_user(name,email,password,role)

def edit_user(current_user,user_id,name,email,role):
    if current_user["role"] != "admin":
        raise PermissionError("You are not allowed to edit user")
    return update_user(user_id,name,email,role)

def remove_user(current_user,user_id):
    if current_user["role"] != "admin":
        raise PermissionError("You are not allowed to remove user")
    return delete_user(user_id)