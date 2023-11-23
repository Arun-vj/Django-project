import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user ='root',
    passwd = 'Admin'
)

cursor = database.cursor()

cursor.execute("create database crm_db")

print("All done")