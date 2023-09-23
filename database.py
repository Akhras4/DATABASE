import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="aaa",
    database="user"
)
mycursor=mydb.cursor()
mycursor.execute('CREATE TABLE INF (firstname VARCHAR(50), lastname VARCHAR(50),email VARCHAR(255),'
                 'password VARCHAR(255),berth VARCHAR(255) ) ')
