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
        cursor.execute(f"select id, username, email, password from users where email = '{email}'")
        userData = cursor.fetchone()
        if userData == None:
            raise ValueError('Incorrect password or email')
        user = {
            "id": userData[0],
            "username": userData[1],
            "email": userData[2],
            "password": userData[3],
        }
        return user
    except Exception as e:
        raise e

def insertNote(note):
    # tile = note['title'],
    # text = note
    try:
        cursor.execute('''
        create table if not exists notes (
            id serial not null primary key,
            title varchar(255) not null,
            text text not null,
            user_id int not null,
            constraint notes_users foreign key (user_id)
            references users (id) match simple
            on delete set null
            on update cascade
            not valid
            );
        ''')
        cursor.execute(f"insert into notes (title, text, user_id) values ('{note['title']}', '{note['text']}', '{note['userId']}')")
        dbConnection.commit()
        return True
    except Exception as e:
        raise Exception('error inserting the note:', e)
