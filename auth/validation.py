import bcrypt
from termcolor import colored

from database import connection
db = connection.dbConnection
cursor = connection.cursor

class Validation:
    # validate if the user is registered.
    def validateUser(self, email: str, password: str):
        try:
            query = f"select * from users where email = '{email}'"
            cursor.execute(query)
            if not cursor.rowcount >= 1:
                raise ValueError(colored('Incorrect email', 'red'))
            userData = cursor.fetchone()

            # Checking is the password is match.
            if not bcrypt.checkpw(password.encode(), userData[3].encode()):
                raise ValueError(colored('Incorrect password', 'red'))

            # return users.User(userData[1], userData[2], userData[3])
            return userData
        except ValueError as e:
            raise e
        except Exception as e:
            exit('Internal error:', e)

    # validate if a string is empty.
    def valueIsEmpty(self, value: str):
        if len(value.strip()) == 0:
            return True
        return False

    def validateTitle(self, title: str, userId: int):
        try:
            cursor.execute(f"select * from notes where user_id = {userId} and title = '{title}'")
            if cursor.rowcount >= 1:
                raise ValueError('Title already exits')
            return True
        except ValueError as e:
            return False