import mysql.connector
mydb = mysql.connector.connect(
   host = "localhost",
   username = "user",
   passwd = "1234"
  
)
mycursor = mydb.cursor()
try:
    mycursor.execute(
       """CREATE DATABASE alx_book_storeDB;
           USE alx_book_storeDB;
       """
        )
    print(" Database 'alx_book_store' created successfully!")
except ProgrammingError:
    print("A data base with that name already exists")

mydb.commit()
mycursor.close()
mydb.close()
