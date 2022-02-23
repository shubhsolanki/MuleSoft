import sqlite3

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('MOVIE.db')

# cursor object
cursor_obj = connection_obj.cursor()

'''connection_obj.execute("""CREATE TABLE movie(
               
                NAME TEXT(20) NOT NULL,
                LEADACTOR TEXT(20) NOT NULL,
                LEADACTORESS TEXT(20) NOT NULL,
                DIRECTOR TEXT(20) NOT NULL,
                YEAROFRELEASE INT NOT NULL);""")
'''
connection_obj.execute(
	"""INSERT INTO movie  VALUES ("dilvale","saruk_Khan","Kajol","Rohit_shetty",2015)""")
connection_obj.execute(
	"""INSERT INTO movie  VALUES ("simmba","Ranvir_shingh","Sara_ali_khan","Rohit_shetty",2018)""")
connection_obj.execute(
	"""INSERT INTO movie  VALUES ("heropanti","tigershroff","kriti_senon","sabir_khan",2014)""")

connection_obj.commit()


# to select all column we will use
statement = '''SELECT * FROM movie'''

cursor_obj.execute(statement)

print("All the data")
output = cursor_obj.fetchall()
for row in output:
    print(row)

connection_obj.commit()


# Close the connection
connection_obj.close()

