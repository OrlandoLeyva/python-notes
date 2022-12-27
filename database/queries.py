from database import connection

dbConnection = connection.dbConnection

duplicateEmailMessage = 'duplicate key value violates unique constraint "users_email_u"'

cursor = connection.cursor

def insertUser(username: str, email: str, password: str):
    try:
        cursor.execute(f"insert into users (username, email, password) values (%s, %s, %s) ", (username, email, password))
        dbConnection.commit()
        return 'success'
    except Exception as e:
        raise ValueError(e)

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

# QUERIES ON NOTES TABLE
def insertNote(note):
    # tile = note['title'],
    # text = note
    try:
        createNotesTable()
        cursor.execute(f"insert into notes (title, text, user_id) values ('{note['title']}', '{note['text']}', '{note['userId']}')")
        dbConnection.commit()
        return True
    except Exception as e:
        raise Exception('error inserting the note:', e)

def getNotesByUserId(userId: int):
    try:
        cursor.execute(f"select * from notes where user_id = {userId}")
        notes = cursor.fetchall()
        return notes
    except Exception as e:
        raise Exception('Error getting notes: ', e)

def removeNote(title: str):
    try:
        cursor.execute(f"delete from notes where title = '{title}'")
        dbConnection.commit()
    except Exception as e:
        raise Exception('Error removing note: ', e)
        
def createNotesTable():
    try:
        cursor.execute('''
        create table if not exists notes (
            id serial not null primary key,
            title varchar(255) not null unique,
            text text not null,
            user_id int not null,
            constraint notes_users foreign key (user_id)
            references users (id) match simple
            on delete set null
            on update cascade
            not valid
            );
        ''')
        dbConnection.commit()
    except Exception as e:
        raise Exception('Error creating notes table:', e)

def validateNoteTitle(title: str):
    try:
        createNotesTable()
        cursor.execute(f"select * from notes where title = '{title}'")
        if cursor.rowcount >= 1:
            raise ValueError('Tile already taken')
        else:
            return True
    except ValueError as e:
        raise(e)
    except Exception as e:
        raise(e)
    

    

