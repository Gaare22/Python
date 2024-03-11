import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "db_tiket"
)

mycursor = mydb.cursor()