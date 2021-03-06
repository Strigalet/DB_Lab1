import psycopg2

connection = psycopg2.connect("dbname=postgres user=postgres password=password")

cursor = connection.cursor()
cursor.execute("DROP TABLE zno")
cursor.execute("DROP TABLE zno_temp")
cursor.close()
connection.commit()
connection.close()
