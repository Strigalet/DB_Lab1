import csv
import os
import psycopg2


sql_query = '''
    SELECT 
        zno_year,
        REGNAME,
        round(avg(UkrBall100),3),
        round(avg(UkrBall12),3),
        round(avg(UkrBall),3)
        
    FROM zno 
    WHERE UkrTestStatus = 'Зараховано' 
    GROUP BY zno_year, REGNAME
'''

bars = ['Year', 'Region', 'ZNO Grade', 'DPA Grade', 'Test Grade']
result = 'result.csv'


def select(connection):
    cursor = connection.cursor()

    cursor.execute(sql_query)
    curfetchall = cursor.fetchall()

    with open(os.path.join('data',result), 'w', newline='') as csvf:
        csv_w = csv.writer(csvf, dialect='excel')
        csv_w.writerow(bars)
        csv_w.writerows(curfetchall)

    cursor.close()

connection = psycopg2.connect("dbname=postgres user=postgres password=password")
select(connection)
connection.close()
