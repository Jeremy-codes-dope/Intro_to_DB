import mysql.connector
mydb = mysql.connector.connect(
   host = "localhost",
   username = "user",
   passwd = "1234"
  
)
mycursor = mydb.cursor()
try:
    mycursor.execute(
       """CREATE DATABASE IF EXISTS alx_book_store;
           USE alxbookstore;
       """
        )
    print(" Database 'alx_book_store' created successfully!")
except Error as e:
    print("A data base with that name already exists")

mydb.commit()
mycursor.close()
mydb.close()
