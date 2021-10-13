import mysql.connector
import config

prefix = "MySQL:"

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