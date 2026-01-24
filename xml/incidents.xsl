<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="/">
        <html>
        <head>
            <title>Incidents List</title>
            <style>
                table {
                    border-collapse: collapse;
                    width: 90%;
                }
                th, td {
                    border: 1px solid black;
                    padding: 8px;
                }
                th {
                    background-color: #b30000;
                    color: white;
                }
                .OPEN {
                    background-color: #ffe6e6;
                }
                .RESOLVED {
                    background-color: #e6ffe6;
                }
            </style>
        </head>
        <body>

            <h2>Incidents</h2>

            <table>
                <tr>
                    <th>ID</th>
                    <th>Title</th>
                    <th>Description</th>
                    <th>Status</th>
                    <th>User ID</th>
                </tr>

                <xsl:for-each select="incidents/incident">
                    <tr class="{status}">
                        <td><xsl:value-of select="@id"/></td>
                        <td><xsl:value-of select="title"/></td>
                        <td><xsl:value-of select="description"/></td>
                        <td><xsl:value-of select="status"/></td>
                        <td><xsl:value-of select="user_id"/></td>
                    </tr>
                </xsl:for-each>
            </table>

        </body>
        </html>
    </xsl:template>

</xsl:stylesheet>
