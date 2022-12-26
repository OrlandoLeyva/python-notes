from database import queries

def register(username:str, email: str, password: str):
    try:
        validateCredential(email, password, 'register', username)
        return queries.insertUser(username, email, password)
    except Exception as e:
        raise e
     
def login(email, password):
    try:
        validateCredential(email, password, 'login')
        user = queries.getUserByEmail(email)
        if not user['password'] == password:
           raise ValueError('Incorrect password or email, try again')
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
