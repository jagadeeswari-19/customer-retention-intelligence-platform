import mysql.connector


def connect_mysql():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jagadeeswari@2004",
        database="funnel_analysis_system"
    )

    return connection

