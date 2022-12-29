from termcolor import colored
import bcrypt

from auth import validation
from database import connection
from models import users

db = connection.dbConnection
cursor = connection.cursor

validation = validation.Validation()

class Auth:
    def register(self):
        username = self.getCredential('username')
        email = self.getCredential('email')
        password = self.getCredential('password')
        hashedPassword = self.hashPassword(password)
        user = users.User(username, email, hashedPassword)
        user.save()

    def login(self):
        while True:
            email = self.getCredential('email')
            password = self.getCredential('password')

            # Returns the user if the credentials are valid.
            try:
                # global user
                userData = validation.validateUser(email, password)
                print(colored(f"\nWelcome inside, {userData[1]}. Let's get started", 'green'))
                break
            except ValueError as e:
                print('\n' + str(e))
        return userData

    def getCredential(self, credential: str):
        value = input(f'Insert {credential}: ')
        while validation.valueIsEmpty(value):
            print(colored(f'\n{credential} cannot be empty', 'red'))
            value = input(f'Insert {credential}: ')
        return value

    def hashPassword(self, password: str):
        return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt()).decode()
