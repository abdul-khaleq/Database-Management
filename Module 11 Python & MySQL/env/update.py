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
                UPDATE students SET name = 'AK' WHERE name = 'Abdul Khaleq'
            """
mycursor.execute(mysqlquery)
mydbconnection.commit()
print("Inserted")