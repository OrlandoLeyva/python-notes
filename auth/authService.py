from database import queries

def register(username:str, email: str, password: str):
    try:
        validateCredential(email, password, 'register', username)
        return queries.insertUser(username, email, password)
    except Exception as e:
        return e
     
def login(email, password):
    try:
        validateCredential(email, password, 'login')
        user = queries.getUserByEmail(email)
        if not user['password'] == password:
           raise Exception('Incorrect password or email, try again')
        return f"welcome back, {user['username']}"
    except Exception as e:
            print('email', type(e))
            return e

def validateCredential(email: str, password: str, request, username = '' ):
    if request == 'register':
        if len(username) == 0:
            raise Exception('username cannot be empty')
    if len(email) == 0:
        raise Exception('email cannot be empty')
    if len(password) == 0:
        raise Exception('password cannot be empty')
    return True

def GetCredentials(request: str):
    userCredentials = {}
    if request == 'register':
        userCredentials['username'] = input('Insert your username: ')
    userCredentials['email'] = input('Insert your email: ')
    userCredentials['password'] = input('Insert your password: ')
    return userCredentials
