import mysql.connector

config = {
    'user': 'root',
    'password': 'YOUR PASSWORD',
    'host': 'localhost',
    'database': 'acme'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()