import sqlite3

#connect to the SQLite database
connection=sqlite3.connect('data_students.db')

## Create a cursor object using the connection
cursor=connection.cursor()

# Create a table 
table_info = """
Create table STUDENT (NAME VARCHAR (25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

# Insert some more records 
cursor.execute(''' Insert into STUDENT values ('Anvesha','Data Science','A',90)''')
cursor.execute(''' Insert into STUDENT values ('Lilavati','Devops','B',99)''')
cursor.execute(''' Insert into STUDENT values ('Vikash','Data Science','A',90)''')
cursor.execute(''' Insert into STUDENT values ('Dipesh','Data Science','A',90)''')

# Display all the records
data = cursor.execute(''' Select * from STUDENT''')

for row in data:
    print(row)

## Close the connection
connection.commit()
connection.close()
