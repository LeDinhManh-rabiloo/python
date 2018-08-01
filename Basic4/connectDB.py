import psycopg2
conn = psycopg2.connect(database='Itplusdb',user = 'postgres',password='manhg@290198',host='127.0.0.1',port='5432')
print(conn)
