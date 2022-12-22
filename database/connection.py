import psycopg2

try:
    dbConnection = psycopg2.connect(
    host='localhost',
    user='postgres_admin',
    password='12ps34ql',
    database='python_notes'
    )

    cursor = dbConnection.cursor()
except Exception as e:
    if type(e) == psycopg2.OperationalError:
        print("we're having internal troubles. please try again in a few minutes")