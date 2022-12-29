from termcolor import colored

from database import connection

db = connection.dbConnection
cursor = connection.cursor


class Note:
    def __init__(self, title: str, text: str, userId) -> None:
        self.title = title
        self.text = text
        self.userId = userId

    def save(self):
        try:
            query = f"insert into notes (title, text, user_id) values ('{self.title}','{self.text}','{self.userId}')"
            cursor.execute(query)
            db.commit()
        except Exception as e:
            exit('internal error')