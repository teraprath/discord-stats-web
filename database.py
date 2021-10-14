import mysql.connector
import config

mydb = mysql.connector.connect(
    host = config.host,
    user = config.user,
    password = config.password,
    database = config.database
)

cursor = mydb.cursor()

def list():
    cursor = mydb.cursor(buffered=True)
    cursor.execute("SELECT * FROM user")
    res = cursor.fetchall()
    return res

def list_with(username):
    cursor = mydb.cursor(buffered=True)
    cursor.execute(f"SELECT * FROM user WHERE username LIKE '%{username}%'")
    res = cursor.fetchall()
    return res