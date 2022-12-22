from database import queries

def register(username:str, email: str, password: str):
    # Validate that the data is not empty
    if len(username) == 0:
        raise Exception('username cannot be empty')
    if len(email) == 0:
        raise Exception('email cannot be empty')
    if len(password) == 0:
        raise Exception('password cannot be empty')

    return queries.insertUser(username, email, password)
    
def login():
    'login user'

