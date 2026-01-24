import xml.etree.ElementTree as ET
from dao.user_dao import get_user_all_users
from dao.incident_dao import get_all_incidents

def export_users_to_xml(file_path="xml/users.xml"):
    users = get_user_all_users()
    root = ET.Element("users")

    for u in users:
        user_el = ET.SubElement(root, "user", id=str(u[0]))
        ET.SubElement(user_el, "name").text = u[1]
        ET.SubElement(user_el, "email").text = u[2]
        ET.SubElement(user_el, "role").text = u[3]

    tree = ET.ElementTree(root)

    tree.write(
        file_path,
        encoding="utf-8",
        xml_declaration=True,
    )
    print("user.xml generated successfully")


def add_users_dtd_and_xsl(file_path="xml/users.xml"):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    header = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE users SYSTEM "users.dtd">
<?xml-stylesheet type="text/xsl" href="users.xsl"?>
"""

    # Remove default xml declaration
    content = content.replace(
        '<?xml version=\'1.0\' encoding=\'utf-8\'?>\n', ''
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(header + content)

    print("✅ DTD and XSL linked to users.xml")

def export_incidents_to_xml(file_path="xml/incidents.xml"):
    incidents = get_all_incidents()

    root = ET.Element("incidents")

    for i in incidents:
        inc_el = ET.SubElement(root, "incident", id=str(i[0]))
        ET.SubElement(inc_el, "title").text = i[1]
        ET.SubElement(inc_el, "description").text = i[2]
        ET.SubElement(inc_el, "status").text = i[3]
        ET.SubElement(inc_el, "user_id").text = str(i[4])

    tree = ET.ElementTree(root)
    tree.write(file_path, encoding="utf-8", xml_declaration=True)
    add_dtd_to_incidents_xml()
    print("✅ incidents.xml generated successfully")


def add_dtd_to_incidents_xml():
    with open("xml/incidents.xml", "r", encoding="utf-8") as f:
        content = f.read()

    header = """<?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE incidents SYSTEM "incidents.dtd">
    <?xml-stylesheet type="text/xsl" href="incidents.xsl"?>
    """
    content = content.replace(
        '<?xml version="1.0" encoding="utf-8"?>\n', ''
    )

    with open("xml/incidents.xml", "w", encoding="utf-8") as f:
        f.write(header + content)
