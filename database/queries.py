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

def getUserByEmail(email):
    try:
        cursor.execute(f"select username, password from users where email = '{email}'")
        userData = cursor.fetchone()
        if userData == None:
            raise Exception('Incorrect password or email, try again')
        print(userData)
        user = {
            "username": userData[0],
            "password": userData[1],
        }
        return user
    except Exception as e:
        return e