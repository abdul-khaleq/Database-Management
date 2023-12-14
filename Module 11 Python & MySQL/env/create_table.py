import mysql.connector

db_name = 'python_test_db'
mydbconnection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = db_name
)
mycursor = mydbconnection.cursor()
mysqlquery ="""
                CREATE TABLE students(
                    roll varchar(4),
                    name varchar(50)
                )
            """
mycursor.execute(mysqlquery)
print("Table created")