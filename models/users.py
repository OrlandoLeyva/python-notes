from termcolor import colored

from database import connection
from auth.validation import Validation
from models.notes import Note

db = connection.dbConnection
cursor = connection.cursor
validator = Validation()

actionsMessage = colored('''
available action

- create note (create)
- list notes (list)
- remove note (remove)
- exit (exit)
''', 'cyan'
)

# Redefined to avoid circular import
def valueIsEmpty(value: str):
        if len(value.strip()) == 0:
            return True
        return False

def defineAction():
    print(actionsMessage)
    global action
    action = input('What do you want to do? ').strip().lower()
    
class User:
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password
    
    def save(self):
        try:
            query = f"insert into users (username, email, password) values ('{self.username}', '{self.email}', '{self.password}')"
            cursor.execute(query)
            db.commit()
            print(colored('\n¡Successfully registered!', 'green'))
        except Exception as e:
            if str(e).startswith('duplicate key value violates unique constraint "users_email_u"'):
                db.rollback()
                print(colored('\nemail already taken', 'red'))
                self.email = input('Insert email: ')
                self.save()
            else:
                exit('Internal error')

    def selectAction(self, userId: int):
        defineAction()
        while True:
            if valueIsEmpty(action):
                print(colored('\nSelect an action', 'red'))
                defineAction()

            if action == 'create':
                print('\ncreating new note...')
                self.createNote(userId)
                defineAction()

            if action == 'list':
                print(colored('your notes:\n', 'cyan') )
                self.listNotes(userId)
                defineAction()

            if action == 'remove':
                print('\nremoving note...')
                self.removeNote(userId)
                defineAction()

            if action == 'exit':
                exit('bye')

            if not action in ['create', 'list', 'remove', 'exit']:
                print('\nselect an available action')
                defineAction()

    def createNote(self, userId: int):
        # Create a valid title.
        while True:
            title = input('Insert the title: ')
            if validator.valueIsEmpty(title):
                print(colored('\ntitle cannot be empty', 'red'))
            else:
                if not validator.validateTitle(title, userId):
                    print(colored(f"\nTitle '{title}' already exists", 'red'))
                else:
                    break
        
        # Create a valid text
        while True:
            text = input('Insert the text: ')
            if validator.valueIsEmpty(text):
                print(colored('\ntext cannot be empty', 'red'))
            else:
                note = Note(title, text, userId)
                note.save()
                print(colored(f"\nNote '{note.title}' successfully created", 'green'))
                break

    def listNotes(self, userId: int):
        try:
            cursor.execute(f"select * from notes where user_id = {userId}") 
            notes = cursor.fetchall()
            if cursor.rowcount == 0:
                    print(f'Any note created yet, do you want to create one now. yes/no: ')
            else:
                for note in notes:
                    print(colored('---------------', 'cyan'))
                    print(f'Title: {note[1]}')
                    print(f'Text: {note[2]}')
        except Exception as e:
            exit('Internal error')
        
    def removeNote(self, userId: int):
        while True:
            try:
                title = input('Insert the tile: ')
                if validator.valueIsEmpty(title):
                    print(colored('\nTitle cannot be empty', 'red'))
                else:
                    cursor.execute(f"delete from notes where user_id = {userId} and title = '{title}'")
                    db.commit()
                    if cursor.rowcount >= 1:
                        print(colored(f"\nNote '{title}' successfully removed", 'green'))
                        break
                    else:
                        print(colored(f"\nnote '{title}' does not exit", 'red'))
                        break
            except Exception as e:
                exit('Internal error')