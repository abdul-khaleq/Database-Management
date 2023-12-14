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
                INSERT INTO students(roll,name) VALUES ('101', 'Abdul Khaleq')
            """
mycursor.execute(mysqlquery)
mydbconnection.commit()
print("Table inserted")