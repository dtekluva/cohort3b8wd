#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect(host='localhost',
                    user='root',
                    password='',
                    database='store',
                    cursorclass=pymysql.cursors.DictCursor)

# prepare a cursor object using cursor() method
# cursor = db.cursor()

# # execute SQL query using execute() method.
# cursor.execute("SELECT * FROM `customers`")

# # Fetch a single row using fetchone() method.
# data = cursor.fetchone()
# print ("Database version : %s " % data)

# # disconnect from server
# db.close()


cursor = db.cursor()

# cursor.execute("""CREATE TABLE EMPLOYEE (
#                 id INT(3) PRIMARY KEY AUTO_INCREMENT NOT NULL,
#                 FIRST_NAME  CHAR(20) NOT NULL,
#                 LAST_NAME  CHAR(20),
#                 AGE INT,  
#                 SEX CHAR(1),
#                 INCOME FLOAT )"""
#                 )

# cursor.close()

for i in range(26):

    # Prepare SQL query to INSERT a record into the database.
    sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
    LAST_NAME, AGE, SEX, INCOME)
    VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
    
    # Prepare SQL query to INSERT a record into the database.
    sqel = """INSERT INTO EMPLOYEE(FIRST_NAME,
    LAST_NAME, AGE, SEX, INCOME)
    VALUES ('john', 'Ham', 30, 'M', 8000)"""

    try:
    # Execute the SQL command
        cursor.execute(sql)
        cursor.execute(sqel)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()