import bcrypt

from database import queries

def register(username:str, email: str, password: str):
    try:
        validateCredential(email, password, 'register', username)
        hashedPassword = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        # Decode the hashed password to avoid it gets encode twice.
        return queries.insertUser(username, email, hashedPassword.decode())
    except ValueError as e:
        raise e
    except Exception as e:
        raise e
     
def login(email: str, password: str):
    try:
        # Validates if the credentials are not empty.
        validateCredential(email, password, 'login')

        # Getting the user by email and validating the password.
        user = queries.getUserByEmail(email) 
        hashedPassword: str = user['password']
        passwordIsCorrect = bcrypt.checkpw(password.encode(), hashedPassword.encode())
        if not passwordIsCorrect:
           raise ValueError('Incorrect password or email')
        
        return user
    except Exception as e:
            raise e

def validateCredential(email: str, password: str, request, username = '' ):
    if request == 'register':
        if len(username) == 0:
            raise ValueError('username cannot be empty')
    if len(email) == 0:
        raise ValueError('email cannot be empty')
    if len(password) == 0:
        raise ValueError('password cannot be empty')
    return True

def GetCredentials(request: str):
    userCredentials = {}
    if request == 'register':
        userCredentials['username'] = input('Insert your username: ')
    userCredentials['email'] = input('Insert your email: ')
    userCredentials['password'] = input('Insert your password: ')
    return userCredentials

