from dao.user_dao import get_user_by_email

def login(email, password):
    user = get_user_by_email(email)

    if not user:
        return None

    if user[3] != password:
        return None

    return {
        'id': user[0],
        'name': user[1],
        'email': user[2],
        'role': user[4]
    }