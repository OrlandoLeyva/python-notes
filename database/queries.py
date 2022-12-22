from database import connection

dbConnection = connection.dbConnection

cursor = connection.cursor

def insertUser(username: str, email: str, password: str):
    try:
        cursor.execute(f"insert into users (username, email, password) values ('{username}', '{email}', '{password}') ")
        dbConnection.commit()
        return 'success'
    except Exception as e:
        return e

