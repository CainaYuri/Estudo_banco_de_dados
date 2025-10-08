import psycopg2

conn = psycopg2.connect(
    database = 'db_Filmes',
    user = 'postgres',
    password = 'C@in@033430',
    host = 'localhost',
    port = '5432'
    )
