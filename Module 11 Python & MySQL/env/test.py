import mysql.connector

mydbconnection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password"
)
print(mydbconnection)
db_name = 'python_test_db'
mycursor = mydbconnection.cursor()
mysqlquery = "CREATE DATABASE " + db_name
mycursor.execute(mysqlquery)