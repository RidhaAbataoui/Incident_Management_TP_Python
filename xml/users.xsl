<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="/">
        <html>
        <head>
            <title>Users List</title>
            <style>
                table {
                    border-collapse: collapse;
                    width: 70%;
                }
                th, td {
                    border: 1px solid black;
                    padding: 8px;
                    text-align: left;
                }
                th {
                    background-color: #333;
                    color: white;
                }
            </style>
        </head>
        <body>
            <h2>Users</h2>

            <table>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Role</th>
                </tr>

                <xsl:for-each select="users/user">
                    <tr>
                        <td><xsl:value-of select="@id"/></td>
                        <td><xsl:value-of select="name"/></td>
                        <td><xsl:value-of select="email"/></td>
                        <td><xsl:value-of select="role"/></td>
                    </tr>
                </xsl:for-each>
            </table>

        </body>
        </html>
    </xsl:template>

</xsl:stylesheet>
