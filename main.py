from services.auth_service import login
from services.user_service import (
    list_users,
    add_user,
    edit_user,
    remove_user
)
from services.incident_service import (
    add_incident,
    list_incidents,
    change_incident_status,
    remove_incident
)
from services.xml_export_service import *

# ---------------- LOGIN ----------------
print("=== Incident Management System ===")
email = input("Email: ")
password = input("Password: ")

current_user = login(email, password)

if not current_user:
    print("❌ Invalid login")
    exit()

print(f"\n✅ Welcome {current_user['name']} ({current_user['role']})")

# ---------------- ADMIN MENU ----------------
def admin_menu():
    while True:
        print("""
--- ADMIN MENU ---
1. List users
2. Add user
3. Update user
4. Delete user
5. List incidents
6. Update incident status
7. Delete incident
8. export users to xml
9. export incidents to xml
0. Logout
""")


        choice = input("Choose an option: ")

        try:
            if choice == "1":
                users = list_users(current_user)
                for u in users:
                    print(u)

            elif choice == "2":
                name = input("Name: ")
                email = input("Email: ")
                password = input("Password: ")
                role = input("Role (admin/employee): ")
                add_user(current_user, name, email, password, role)
                print("✅ User added")

            elif choice == "3":
                user_id = int(input("User ID: "))
                name = input("New name: ")
                email = input("New email: ")
                role = input("Role (admin/employee): ")
                edit_user(current_user, user_id, name, email, role)
                print("✅ User updated")

            elif choice == "4":
                user_id = int(input("User ID: "))
                remove_user(current_user, user_id)
                print("✅ User deleted")

            elif choice == "5":
                incidents = list_incidents(current_user)
                for i in incidents:
                    print(i)

            elif choice == "6":
                incident_id = int(input("Incident ID: "))
                status = input("New status (OPEN / IN_PROGRESS / RESOLVED / CLOSED): ")
                change_incident_status(current_user, incident_id, status)
                print("✅ Incident status updated")

            elif choice == "7":
                incident_id = int(input("Incident ID: "))
                remove_incident(current_user, incident_id)
                print("✅ Incident deleted")

            elif choice == "8":
                export_users_to_xml()
                add_users_dtd_and_xsl()

            elif choice == "9":
                export_incidents_to_xml()
                add_dtd_to_incidents_xml()

            elif choice == "0":
                print("👋 Logout")
                break

            else:
                print("❌ Invalid option")

        except Exception as e:
            print("⚠️ Error:", e)


# ---------------- EMPLOYEE MENU ----------------
def employee_menu():
    while True:
        print("""
--- EMPLOYEE MENU ---
1. Add incident
2. View my incidents
0. Logout
""")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                title = input("Incident title: ")
                description = input("Description: ")
                add_incident(title, description, current_user)
                print("✅ Incident added")

            elif choice == "2":
                incidents = list_incidents(current_user)
                for i in incidents:
                    print(i)

            elif choice == "0":
                print("👋 Logout")
                break

            else:
                print("❌ Invalid option")

        except Exception as e:
            print("⚠️ Error:", e)


# ---------------- ROUTER ----------------
if current_user["role"] == "admin":
    admin_menu()
else:
    employee_menu()

print("System closed.")



















